/*
 * Wheel_Driver.c
 *
 * Created: 12/18/2015 4:45:01 AM
 * Author : BENGEOS-PC
 */ 

#define F_CPU 8000000
#include <avr/io.h>
#include <avr/interrupt.h>
#include "USART.h"
#include <util/delay.h>
#include <string.h>
#include <avr/pgmspace.h>

volatile int i=0;
volatile uint8_t buffer[20];
volatile uint8_t StrRxFlag=0;

ISR(USART0_RX_vect)
{
	buffer[i]=UDR0;         //Read USART data register
	if(buffer[i++]=='\r')   //check for carriage return terminator and increment buffer index
	{
		// if terminator detected
		StrRxFlag=1;        //Set String received flag
		buffer[i-1]=0x00;   //Set string terminator to 0x00
		i=0;                //Reset buffer index
	}
	
}
void Process_CMD(char cmd[]){
	if(strstr(cmd,"p")){
		USART_Put("Key = P\r\n");
		PORTA = 0x03;
		}else if(strstr(cmd,"o")){
		USART_Put("Key = O\r\n");
		PORTA = 0x01;
		}else if(strstr(cmd,"i")){
		USART_Put("Key = I\r");
		PORTA = 0x05;
		}else if(strstr(cmd,"l")){
		USART_Put("Key = L\r");
		PORTA = 0x08;
	}
}
int main(void)
{
	DDRB = 0xFF;
	DDRA = 0xFF;
	
	DDRC = 0x00;
	PORTC = 0X00;

	USART_Init();
	while(1)
	{
		_delay_ms(40);
		//TODO:: Please write your application code
		//USART_send('A');
		if (StrRxFlag){
			//USART_Put(buffer);
			Process_CMD(buffer);
			StrRxFlag=0;
		}else{
			PORTA = 0x00;
		}
	}
}

