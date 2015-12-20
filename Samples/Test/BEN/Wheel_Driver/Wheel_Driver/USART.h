/*
 * USART.h
 *
 * Created: 12/4/2015 6:07:56 PM
 *  Author: BENGEOS-PC
 */ 


#ifndef USART_H_
#define USART_H_
void USART_Init(void);
void USART_send( unsigned char data);
void USART_Put(char* StringPtr);

#endif /* USART_H_ */