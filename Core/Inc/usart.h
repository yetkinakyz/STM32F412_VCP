/*
 * usart.h
 *
 *  Created on: Sep 16, 2021
 *      Author: yetkinakyuz
 */

#ifndef INC_USART_H_
#define INC_USART_H_

#include "stm32f4xx_hal.h"
#include "usb_device.h"

void USART_Main(unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND);

#endif /* INC_USART_H_ */
