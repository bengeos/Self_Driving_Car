/*
 * USART.c
 *
 * Created: 12/4/2015 5:58:10 PM
 *  Author: BENGEOS-PC
 */ 
#define F_CPU 8000000UL
#include <util/delay.h>
#include <avr/io.h>


#define BAUDRATE 9600
#define BAUD_PRESCALER (((F_CPU / (BAUDRATE * 16UL))) - 1)
#include <avr/interrupt.h>


void USART_Init(void)
{
	cli();
	// Macro to determine the baud prescale rate see table 22.1 in the Mega datasheet
	#define BAUD_PRESCALER (((F_CPU / (BAUDRATE * 16UL))) - 1)
	
	UBRR0 = BAUD_PRESCALER;                 // Set the baud rate prescale rate register
	UCSR0B = ((1<<RXEN0)|(1<<TXEN0)|(1 << RXCIE0));       // Enable receiver and transmitter and Rx interrupt
	UCSR0C = ((0<<USBS0)|(1 << UCSZ01)|(1<<UCSZ00));  // Set frame format: 8data, 1 stop bit. See Table 22-7 for details
	sei();
}
void USART_send( unsigned char data)
{
	//while the transmit buffer is not empty loop
	while(!(UCSR0A & (1<<UDRE0)));
	
	//when the buffer is empty write data to the transmitted
	UDR0 = data;
}
void USART_Put(char* StringPtr)
// sends the characters from the string one at a time to the USART
{
	while(*StringPtr != 0x00)
	{
		USART_send(*StringPtr);
		StringPtr++;
	}
}