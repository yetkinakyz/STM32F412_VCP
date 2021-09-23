/*
 * usart.c
 *
 *  Created on: Sep 15, 2021
 *      Author: yetkinakyuz
 */

/* Includes ------------------------------------------------------------------*/
#include "usart.h"

/* External private functions -----------------------------------------------*/
extern uint8_t CDC_Transmit_FS(uint8_t* Buf, uint16_t Len);
extern void data_received(uint8_t* data, uint32_t *Len);

/* Private function prototypes -----------------------------------------------*/
void USART_Transmit(unsigned char peripheralID, unsigned char command);

/* External private variables -----------------------------------------------*/
extern UART_HandleTypeDef huart1;
extern UART_HandleTypeDef huart2;
extern UART_HandleTypeDef huart3;
extern UART_HandleTypeDef huart6;
UART_HandleTypeDef dumb;

/* Private variables -----------------------------------------------*/
extern unsigned char peripheralID;

/* Main USART function */
void USART_Main(unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND)
{
	USART_Transmit(peripheralID, COMMAND);
}

/* USART Transmit function */
void USART_Transmit(unsigned char peripheralID, unsigned char command)
{
	if (peripheralID <= 0x06)
	{
		UART_HandleTypeDef uart[7] = {dumb,huart1,huart2,huart3,dumb,dumb,huart6};
		HAL_UART_Transmit(&(uart[peripheralID]), (uint8_t *)"*", strlen("*"), HAL_MAX_DELAY);
	}
}

