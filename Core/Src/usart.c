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

extern unsigned char peripheralID;

/* Private variables -----------------------------------------------*/
UART_HandleTypeDef dumb;
char *usarts[7] = {"USART0", "USART1", "USART2", "USART3", "USART4", "USART5", "USART6"};
int USART_R[7] = {0,0,0,0,0,0};

/* Main USART function */
void USART_Main(unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND)
{
	char transmit_buffer[40] = "";

	//Transmit
	if(PROCESS == 0x11)
	{
		if(USART_R[peripheralID] == 0)
		{
			sprintf(transmit_buffer, "Message is sent over %s.\n", usarts[peripheralID]);
			CDC_Transmit_FS((uint8_t *)&transmit_buffer, strlen(transmit_buffer));
		}

		USART_Transmit(peripheralID, COMMAND);
	}
	//Receive
	else if(PROCESS == 0x22)
	{
		//Enable Receive
		if(COMMAND == 0x00)
		{
			sprintf(transmit_buffer, "%s receive function is enabled.\n", usarts[peripheralID]);
			CDC_Transmit_FS((uint8_t *)&transmit_buffer, strlen(transmit_buffer));

			USART_R[peripheralID] = 1;
		}
		//Disable Receive
		else
		{
			sprintf(transmit_buffer, "%s receive function is disabled.\n", usarts[peripheralID]);
			CDC_Transmit_FS((uint8_t *)&transmit_buffer, strlen(transmit_buffer));

			USART_R[peripheralID] = 0;
		}
	}
}

/* USART Transmit function */
void USART_Transmit(unsigned char peripheralID, unsigned char command)
{
	if (peripheralID <= 0x06)
	{
		UART_HandleTypeDef usart[7] = {dumb,huart1,huart2,huart3,dumb,dumb,huart6};
		HAL_UART_Transmit(&(usart[peripheralID]), (uint8_t *)"*", strlen("*"), HAL_MAX_DELAY);
	}
}

