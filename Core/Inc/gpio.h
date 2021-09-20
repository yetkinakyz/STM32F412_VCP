/*
 * gpio.h
 *
 *  Created on: Sep 16, 2021
 *      Author: yetkinakyuz
 */

#ifndef INC_GPIO_H_
#define INC_GPIO_H_

#include "stm32f4xx_hal.h"
#include "usb_device.h"

void GPIO_Main(unsigned char peripheralGROUP, unsigned char peripheralID, unsigned char PROCESS, unsigned char COMMAND);

#endif /* INC_GPIO_H_ */
