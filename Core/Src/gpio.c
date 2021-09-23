/*
 * gpio.c
 *
 *  Created on: Sep 15, 2021
 *      Author: yetkinakyuz
 */

/* Includes ------------------------------------------------------------------*/
#include "gpio.h"

/* Private function prototypes -----------------------------------------------*/
extern uint8_t CDC_Transmit_FS(uint8_t* Buf, uint16_t Len);
extern void data_received(uint8_t* data, uint32_t *Len);

GPIO_TypeDef* GPIO_PORT_SELECT(unsigned char peripheralGROUP);
uint16_t GPIO_PIN_SELECT(unsigned char peripheralID);

/* Functions -----------------------------------------------------------------*/
void GPIO_Main(unsigned char peripheralGROUP, unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND)
{
	char GPIO_buffer[64];

	if(PROCESS == 0x11) //Read GPIO
	{
		GPIO_TypeDef* port = GPIO_PORT_SELECT(peripheralGROUP);
		uint16_t pin = GPIO_PIN_SELECT(peripheralID);
		int result = HAL_GPIO_ReadPin(port, pin);

		sprintf(GPIO_buffer, "GPIO state = %d.\n", result);
		CDC_Transmit_FS((uint8_t *)GPIO_buffer, strlen(GPIO_buffer));
	}
	else if(PROCESS == 0x22) //Write GPIO
	{
		if(COMMAND == 0x00) //Reset
		{
			CDC_Transmit_FS((uint8_t *)"GPIO reset.\n", strlen("GPIO reset.\n"));
			HAL_GPIO_WritePin(GPIO_PORT_SELECT(peripheralGROUP), GPIO_PIN_SELECT(peripheralID), GPIO_PIN_RESET);
		}
		else if(COMMAND == 0x01) //Set
		{
			CDC_Transmit_FS((uint8_t *)"GPIO set.\n", strlen("GPIO set.\n"));
			HAL_GPIO_WritePin(GPIO_PORT_SELECT(peripheralGROUP), GPIO_PIN_SELECT(peripheralID), GPIO_PIN_SET);
		}
		else //Error!
		{
			CDC_Transmit_FS((uint8_t *)"Error: Invalid 'GPIO Write' command.\n", strlen("Error: Invalid 'GPIO Write' command.\n"));
		}
	}
	else if(PROCESS == 0x33) //Toggle GPIO
	{
		CDC_Transmit_FS((uint8_t *)"GPIO toggled.\n", strlen("GPIO toggled.\n"));
		HAL_GPIO_TogglePin(GPIO_PORT_SELECT(peripheralGROUP), GPIO_PIN_SELECT(peripheralID));
	}
	else
	{
		CDC_Transmit_FS((uint8_t *)"Error: Invalid GPIO process.\n", strlen("Error: Invalid GPIO process.\n"));
	}
}

/* GPIO PORT SELECTOR */
GPIO_TypeDef* GPIO_PORT_SELECT(unsigned char peripheralGROUP)
{
		 if (peripheralGROUP == 0x10)	{return GPIOA;}
	else if (peripheralGROUP == 0x11)	{return GPIOB;}
	else if (peripheralGROUP == 0x12)	{return GPIOC;}
	else if (peripheralGROUP == 0x13)	{return GPIOD;}
	else if (peripheralGROUP == 0x14)	{return GPIOE;}
	else if (peripheralGROUP == 0x15)	{return GPIOF;}
	else if (peripheralGROUP == 0x16)	{return GPIOG;}
	else //Error!
	{
		CDC_Transmit_FS((uint8_t *)"Error: Invalid 'GPIO Port' selection.\n", strlen("Error: Invalid 'GPIO Port' selection.\n"));
	}

	return 0;
}

/* GPIO PIN SELECTOR */
uint16_t GPIO_PIN_SELECT(unsigned char peripheralID)
{
		 if (peripheralID == 0x00)	{return GPIO_PIN_0;}
	else if (peripheralID == 0x01)	{return GPIO_PIN_1;}
	else if (peripheralID == 0x02)	{return GPIO_PIN_2;}
	else if (peripheralID == 0x03)	{return GPIO_PIN_3;}
	else if (peripheralID == 0x04)	{return GPIO_PIN_4;}
	else if (peripheralID == 0x05)	{return GPIO_PIN_5;}
	else if (peripheralID == 0x06)	{return GPIO_PIN_6;}
	else if (peripheralID == 0x07)	{return GPIO_PIN_7;}
	else if (peripheralID == 0x08)	{return GPIO_PIN_8;}
	else if (peripheralID == 0x09)	{return GPIO_PIN_9;}
	else if (peripheralID == 0x10)	{return GPIO_PIN_10;}
	else if (peripheralID == 0x11)	{return GPIO_PIN_11;}
	else if (peripheralID == 0x12)	{return GPIO_PIN_12;}
	else if (peripheralID == 0x13)	{return GPIO_PIN_13;}
	else if (peripheralID == 0x14)	{return GPIO_PIN_14;}
	else if (peripheralID == 0x15)	{return GPIO_PIN_15;}
	else if (peripheralID == 0x16)	{return GPIO_PIN_All;}
	else //Error!
	{
		CDC_Transmit_FS((uint8_t *)"Error: Invalid 'GPIO Pin' selection.\n", strlen("Error: Invalid 'GPIO Pin' selection.\n"));
	}

	return 0;
}
