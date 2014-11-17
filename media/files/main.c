/*
 * Adam Gauthier (atg3ee) George "Ramses" Luo (gl5ed)
 * Felix Cao (fdc2gz)	  Ronnie Smith (rls8ru)
 * This program spins a motor in alternating directions, using pwm to accelerate and decelerate
 * at the beginning of each cycle. After a cycle, the direction changes and the cycle repeats.
 * The correction algorithm has the wheel stop earlier or later each time to account for the intertia
 * that causes the wheel to stop in a place farther than where the stop command was sent. If the wheel
 * is told to stop after one revolution, it will actually stop somehwere around 1 and 1/5 revolutions, so
 * the next cycle it will stop 1/5 of a revolution early.
 */
#include <msp430.h>

#define TOTALSPINS		5
#define AIN1			BIT3		//input pins to control voltages
#define AIN2			BIT4
#define STBY			BIT1
#define PWMA 			BIT2
#define outA			BIT4		//Encoder A (port 2)
#define outB			BIT3		//Encoder B (port 2)
#define Button			BIT3		//Button p1.3
#define RedLed 			BIT0		//RedLed = BIT0
#define GreenLed		BIT6		//GreenLed = BIT6

typedef enum { //enum for state machine values
	high,low
}EncoderSignal;

typedef enum {				//Type def for the state machine
	AlowBlow, AhighBlow, AlowBhigh, AhighBhigh, Initialize
} EncoderState;

typedef struct { //struct to handle both values of encoder count
	EncoderSignal a;
	EncoderSignal b;
}Encoder;


void initialize(void);
void init_timer(void);
void init_ports(void);
void write(char byte);
void spin_motor(void);
void ramp_down(void);
void read_encoder(void);
void cw(void);
void ccw(void);
void stop(void);
EncoderSignal getSwitchA();
EncoderSignal getSwitchB();

char dir = 1;	//keep track of direction
Encoder myEncoder;	//keep track of encoder state
int msCount = 0;	//10 ms counter for stop delay time
EncoderState myState = Initialize; //starting state
long count = 0;	//keep track of total encoder clicks
int count2 = 0;	//keep track of each revolution to blink led
long target = 465*TOTALSPINS; //total clicks for however many spins, changes according to adjustment
long first = 465*TOTALSPINS; //original number of total clicks
int rev = 465; //number of spins in a revolution
int rampNum = 78; //number of clicks in rampingg
long extra = 0; //adjustment needed for each time direction is changed
char up = 1; //ramping up or down
char stopped = 0; //stopped yes or no
char ramping = 1; //ramping or not
int main(void) {
    WDTCTL = WDTPW | WDTHOLD;	// Stop watchdog timer
	initialize(); //set up ports and timer
	_BIS_SR(GIE); //enable global variables
	while (1) {
		if(count2 >= 465) { //if spun one revoultion blink led
			P1OUT ^= GreenLed;
			count2 = 0; //reset count
		}
		read_encoder(); //continuously read encoder values
		if(stopped) {
			int timestamp = msCount;
			while(msCount - timestamp < 800) { // wait a second, and during this time read encoder
				read_encoder(); //inertia will cause wheel to keep spinning so get extra ticks
			}
			msCount = 0; //reset count
			stopped = 0; //not stopped
			TA1CTL |= MC_1; //restart timer to pwm
		}
		if(dir) {
			if(count > target) { //spun as many times as i want
				if(count > first) {
					extra = count - first; //see how far ideal stopping point wheel went
					target = target - extra; //adjust target to stop earlier so end result is where wheel started
				}
				if(count < first) {
					extra = first - count; //in case i have a negative amount to adjust
					target = target + extra;
				}
				count = 0; //reset count
				dir ^= 1; //switch direction
			}
		}
		else {
			if(count*-1 > target) { //counting down, if max ticks is reached, stop
				count *= -1;
				if(count > first) {
					extra = count - first; //see how far ideal stopping point wheel went
					target = target - extra; //adjust target to stop earlier so end result is where wheel started
				}
				if(count < first) {
					extra = first - count;
					target = target + extra;
				}
				count = 0; //reset count to count up
				dir ^= 1;
			}
		}
	}
	return 0;
}
//don't need this anymore
void stop(void) {
	P1OUT |= PWMA + STBY;
	P1OUT &= ~(AIN1 + AIN2);
	int timestamp = msCount;
	while(msCount - timestamp < 100) {
		read_encoder();
	}
	msCount = 0;
}

void cw(void) {
	P1OUT |= AIN1 + PWMA + STBY; //set proper bits to high or low to spin cw
	P1OUT &= ~AIN2;
}
void ccw(void) {
	P1OUT &= ~AIN1;
	P1OUT |= AIN2 + PWMA + STBY; //set proper bits to high or low to spin ccw
}
//set proper bits to stop motor depending on direction
void short_brake(void) {
	switch(dir) {
	case 1: //cw
		P1OUT |= AIN2 + STBY;
		P1OUT &= ~(AIN1 + PWMA);
		break;
	case 0: //ccw
		P1OUT |= AIN1 + STBY;
		P1OUT &= ~(AIN2 + PWMA);
		break;
	}
}
void read_encoder(void) {
	myEncoder.a = getSwitchA();
	myEncoder.b = getSwitchB();
	switch (myState) {//switch statement is used to implement state machine
	case Initialize:											//First state

		if (myEncoder.a == high && myEncoder.b  == high)
			myState = AhighBhigh;		//if output is 11 go to AhighBhigh
		if (myEncoder.a == high && myEncoder.b  == low)
			myState = AhighBlow;			//if output is 10 go to AhighBlow
		if (myEncoder.a == low && myEncoder.b  == high)
			myState = AlowBhigh;			//if output is 01 got to AlowBhigh
		if (myEncoder.a == high && myEncoder.b  == high)
			myState = AhighBhigh;		//if output is 00 go to AlowBlow
		break;
	case AlowBlow:												// 00	 state
		if (myEncoder.a == high) {
			count ++;
			count2++;
			myState = AhighBlow;						//change state to 10
		}
		if (myEncoder.b  == high) {
			count--;
			count2++;
			myState = AlowBhigh;						//state is now 01
		}
		break;
	case AlowBhigh:											//if 01
		if (myEncoder.a == high) {
			count--;
			count2++;
			myState = AhighBhigh;					//state is now 11
		}
		if (myEncoder.b  == low) {
			count++;
			count2++;
			myState = AlowBlow;		 				//now switch to 00
		}
		break;
	case AhighBlow:										//for state 10
		if (myEncoder.a == low) {
			myState = AlowBlow;					//change state to now 00
			count--;
			count2++;
		}
		if (myEncoder.b  == high) {
			count++;
			count2++;
			myState = AhighBhigh;				//state is now 11
		}
		break;
	case AhighBhigh:									//for state 11
		if (myEncoder.a == low) {
			count++;
			count2++;
			myState = AlowBhigh;					//change state to 01
		}
		if (myEncoder.b  == low) {
			count--;
			count2++;
			myState = AhighBlow;					//change to 10 state
		}
		break;
	default:											//set default incase of error
		myState = Initialize;					//goes to initalize
	}
	if((count >= target - rampNum) || (count*-1 >= target - rampNum))
		ramping = 1;
}
void spin_motor(void) {
		switch(dir) {
		case 1 : //cw
			cw();
			break;
		case 0 : //ccw
			ccw();
			break;
		}
}

#pragma vector=TIMER0_A0_VECTOR
__interrupt void TimerA0_routine(void) {
	msCount++; //counter for delay while stopped
}
//pwm timer to turn on motor
#pragma vector=TIMER1_A0_VECTOR
__interrupt void TimerA1_routine(void) {
	if(ramping) { //if ramping
		if(up) {
			TA1CCR1 += 13; //increment ccr1 up to ccr0, max ratio of pwm
			if(TA1CCR1 >= TA1CCR0) {
				ramping = 0; //no longer rampnig
				up =  0; //next time we ramp going down
			}
			spin_motor();
		}
		else {
			TA1CCR1 -= 13; //increment ccr1 down to 0, min ratio of pwm
			if(TA1CCR1 > 0)
				spin_motor();
			else {
				ramping = 0; //done ramping
				up = 1; //next time we ramp going up
				stopped = 1; //stopped, so check encoder and take care of correction
			}
		}
	}
	else
		spin_motor(); //spinning at max speed
	if(stopped)
		TA1CTL &= ~MC_1; //stop timer when done spinning so we can take care of correction
	TA1CCTL0 &= ~(CCIFG);//clear the interrupt flag so another interrupt can be called
}
//pwm to stop timer
#pragma vector=TIMER1_A1_VECTOR
__interrupt void TimerA2_routine(void) {
	if(ramping)
		P1OUT &= ~STBY; //stop spinning
	TA1CCTL1 &= ~(CCIFG);//clear the interrupt flag so another interrupt can be called

}
EncoderSignal getSwitchA() {			//reads switchA pin and set its high or low
	EncoderSignal temp;						//temperary value
	char state = P2IN & outA;					//read the value at pin 2.4
	if (state == outA)						//if it is = to 1
		temp = high;						//set high
	else if (state == 0x00)					//if it is = to 0
		temp = low;							//set low
	return temp;							//return state
}

EncoderSignal getSwitchB () {			//reads b  pin and set its high or low
	EncoderSignal temp;						//temperary value
	char state = P2IN & outB;					//read the value at pin 2.3.
	if (state == outB)						//if it is = to 1
		temp = high;						//set high
	else if (state == 0x00)					//if it is = to 0
		temp = low;							//set low
	return temp;							//return state
}
void initialize(void) {
	init_ports();
	init_timer();
}
void init_timer(void) {
	DCOCTL = CALDCO_16MHZ; 		//DC Clock Frequency Control
	BCSCTL1 = CALBC1_16MHZ; 		//Basic Clock System Control
	
	TA0CCR0 = 20480;
	TA0CCTL0 = CCIE | CM_0; 		//no capture, just control
	TA0CTL = TASSEL_2  | TACLR | MC_1; //sm clock, divide timer frequency by 8, clear the timer, clock is in up mode

	TA1CCR0 = 1000;
	TA1CCR1 = 0;
	TA1CCTL0 = CCIE | CM_0;
	TA1CCTL1 = CCIE | CM_0;			//no capture, just control
	TA1CTL = TASSEL_2 | TACLR | MC_1;
}

void init_ports(void) {
	P1OUT = 0x00;
	P2OUT = 0x00;
	P1DIR |= GreenLed + RedLed + AIN1 + AIN2 + STBY + PWMA;
	P1DIR &= ~Button;
	P1OUT |= Button;
	P2DIR &= ~(outA + outB);
	P1REN |= Button;
}
