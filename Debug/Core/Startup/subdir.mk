################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
S_SRCS += \
../Core/Startup/startup_stm32f412zgtx.s 

OBJS += \
./Core/Startup/startup_stm32f412zgtx.o 

S_DEPS += \
./Core/Startup/startup_stm32f412zgtx.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Startup/startup_stm32f412zgtx.o: ../Core/Startup/startup_stm32f412zgtx.s Core/Startup/subdir.mk
	arm-none-eabi-gcc -mcpu=cortex-m4 -g3 -c -I"/Users/yetkinakyuz/ARM Projects/f412_vcp/USB_DEVICE" -x assembler-with-cpp -MMD -MP -MF"Core/Startup/startup_stm32f412zgtx.d" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@" "$<"

