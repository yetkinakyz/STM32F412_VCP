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
void USART_Transmit(unsigned char peripheralID);

/* External private variables -----------------------------------------------*/
extern UART_HandleTypeDef huart1;
extern UART_HandleTypeDef huart2;
extern UART_HandleTypeDef huart3;
extern UART_HandleTypeDef huart6;

/* Private variables -----------------------------------------------*/
extern unsigned char peripheralID;

/* Main USART function */
void USART_Main(unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND)
{
	USART_Transmit(peripheralID);
}

/* USART Transmit function */
void USART_Transmit(unsigned char peripheralID)
{
	if(peripheralID == 0x01) //uart1
	{
		HAL_UART_Transmit(&huart1, (uint8_t *)"0", strlen("0"), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x02) //uart2
	{
		HAL_UART_Transmit(&huart2, (uint8_t *)"0", strlen("0"), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x03) //uart3
	{
		HAL_UART_Transmit(&huart3, (uint8_t *)"0", strlen("0"), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x06) //uart6
	{
		HAL_UART_Transmit(&huart6, (uint8_t *)"0", strlen("0"), HAL_MAX_DELAY);
	}

	else
	{
		CDC_Transmit_FS((uint8_t *)"Error: Invalid USART selection.\n", strlen("Error: Invalid USART selection.\n"));
	}
}
