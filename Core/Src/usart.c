/*
 * usart.c
 *
 *  Created on: Sep 15, 2021
 *      Author: yetkinakyuz
 */

/* Includes ------------------------------------------------------------------*/
#include "usart.h"

/* Private function prototypes -----------------------------------------------*/
extern uint8_t CDC_Transmit_FS(uint8_t* Buf, uint16_t Len);
extern void data_received(uint8_t* data, uint32_t *Len);
void USART_SELECT(unsigned char peripheralID);

/* Private variables -----------------------------------------------*/
extern UART_HandleTypeDef huart1;
extern UART_HandleTypeDef huart2;
extern UART_HandleTypeDef huart3;
extern UART_HandleTypeDef huart6;

extern unsigned char peripheralID;

UART_HandleTypeDef* selected_usart;

void USART_FUNC(unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND)
{
	if(peripheralID == 0x01)
	{
		HAL_UART_Transmit(&huart1, (uint8_t *)"0", strlen("0"), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x02)
	{
		HAL_UART_Transmit(&huart2, (uint8_t *)&COMMAND, sizeof(COMMAND), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x03)
	{
		HAL_UART_Transmit(&huart3, (uint8_t *)&COMMAND, sizeof(COMMAND), HAL_MAX_DELAY);
	}

	else if(peripheralID == 0x06)
	{
		HAL_UART_Transmit(&huart6, (uint8_t *)&COMMAND, sizeof(COMMAND), HAL_MAX_DELAY);
	}

	else
	{
		CDC_Transmit_FS((uint8_t *)"Error: Invalid USART selection.\n", strlen("Error: Invalid USART selection.\n"));
	}
}
