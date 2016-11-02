import time

class LightSensor:
  TSL2591_VISIBLE           =2        # channel 0 - channel 1
  TSL2591_INFRARED          =1        # channel 1
  TSL2591_FULLSPECTRUM      =0        # channel 0
  TSL2591_ADDR              =0x29
  TSL2591_READBIT           =0x01
  TSL2591_COMMAND_BIT       =0xA0     # 1010 0000: bits 7 and 5 for 'command normal'
  TSL2591_CLEAR_INT         =0xE7
  TSL2591_TEST_INT          =0xE4
  TSL2591_WORD_BIT          =0x20     # 1 = read/write word  =rather than byte)
  TSL2591_BLOCK_BIT         =0x10     # 1 = using block read/write
  TSL2591_ENABLE_POWEROFF   =0x00
  TSL2591_ENABLE_POWERON    =0x01
  TSL2591_ENABLE_AEN        =0x02     # ALS Enable. This field activates ALS function. Writing a one activates the ALS. Writing a zero disables the ALS.
  TSL2591_ENABLE_AIEN       =0x10     # ALS Interrupt Enable. When asserted permits ALS interrupts to be generated subject to the persist filter.
  TSL2591_ENABLE_NPIEN      =0x80     # No Persist Interrupt Enable. When asserted NP Threshold conditions will generate an interrupt bypassing the persist filter
  TSL2591_LUX_DF            =408.0
  TSL2591_LUX_COEFB         =1.64      # CH0 coefficient 
  TSL2591_LUX_COEFC         =0.59      # CH1 coefficient A
  TSL2591_LUX_COEFD         =0.86      # CH2 coefficient B
  TSL2591_REGISTER_ENABLE             = 0x00
  TSL2591_REGISTER_CONTROL            = 0x01
  TSL2591_REGISTER_THRESHOLD_AILTL    = 0x04 # ALS low threshold lower byte
  TSL2591_REGISTER_THRESHOLD_AILTH    = 0x05 # ALS low threshold upper byte
  TSL2591_REGISTER_THRESHOLD_AIHTL    = 0x06 # ALS high threshold lower byte
  TSL2591_REGISTER_THRESHOLD_AIHTH    = 0x07 # ALS high threshold upper byte
  TSL2591_REGISTER_THRESHOLD_NPAILTL  = 0x08 # No Persist ALS low threshold lower byte
  TSL2591_REGISTER_THRESHOLD_NPAILTH  = 0x09 # etc
  TSL2591_REGISTER_THRESHOLD_NPAIHTL  = 0x0A
  TSL2591_REGISTER_THRESHOLD_NPAIHTH  = 0x0B
  TSL2591_REGISTER_PERSIST_FILTER     = 0x0C
  TSL2591_REGISTER_PACKAGE_PID        = 0x11
  TSL2591_REGISTER_DEVICE_ID          = 0x12
  TSL2591_REGISTER_DEVICE_STATUS      = 0x13
  TSL2591_REGISTER_CHAN0_LOW          = 0x14
  TSL2591_REGISTER_CHAN0_HIGH         = 0x15
  TSL2591_REGISTER_CHAN1_LOW          = 0x16
  TSL2591_REGISTER_CHAN1_HIGH         = 0x17
  TSL2591_INTEGRATIONTIME_100MS     = 0x00
  TSL2591_INTEGRATIONTIME_200MS     = 0x01
  TSL2591_INTEGRATIONTIME_300MS     = 0x02
  TSL2591_INTEGRATIONTIME_400MS     = 0x03
  TSL2591_INTEGRATIONTIME_500MS     = 0x04
  TSL2591_INTEGRATIONTIME_600MS     = 0x05
  #  bit 7:4: 0
  TSL2591_PERSIST_EVERY             = 0x00 # Every ALS cycle generates an interrupt
  TSL2591_PERSIST_ANY               = 0x01 # Any value outside of threshold range
  TSL2591_PERSIST_2                 = 0x02 # 2 consecutive values out of range
  TSL2591_PERSIST_3                 = 0x03 # 3 consecutive values out of range
  TSL2591_PERSIST_5                 = 0x04 # 5 consecutive values out of range
  TSL2591_PERSIST_10                = 0x05 # 10 consecutive values out of range
  TSL2591_PERSIST_15                = 0x06 # 15 consecutive values out of range
  TSL2591_PERSIST_20                = 0x07 # 20 consecutive values out of range
  TSL2591_PERSIST_25                = 0x08 # 25 consecutive values out of range
  TSL2591_PERSIST_30                = 0x09 # 30 consecutive values out of range
  TSL2591_PERSIST_35                = 0x0A # 35 consecutive values out of range
  TSL2591_PERSIST_40                = 0x0B # 40 consecutive values out of range
  TSL2591_PERSIST_45                = 0x0C # 45 consecutive values out of range
  TSL2591_PERSIST_50                = 0x0D # 50 consecutive values out of range
  TSL2591_PERSIST_55                = 0x0E # 55 consecutive values out of range
  TSL2591_PERSIST_60                = 0x0F # 60 consecutive values out of range
  TSL2591_GAIN_LOW                  = 0x00    # low gain (1x)
  TSL2591_GAIN_MED                  = 0x10    # medium gain (25x)
  TSL2591_GAIN_HIGH                 = 0x20    # high gain (428x)
  TSL2591_GAIN_MAX                  = 0x30    # max gain (9876x) 
  def __init__ (self, i2c, id):
      self.__i2c = i2c
      self.__id = LightSensor.TSL2591_ADDR #id
      self.__integration = LightSensor.TSL2591_INTEGRATIONTIME_100MS
      self.__gain = LightSensor.TSL2591_GAIN_MED
  def enable (self):
      msg = bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_ENABLE, LightSensor.TSL2591_ENABLE_POWERON | LightSensor.TSL2591_ENABLE_AEN | LightSensor.TSL2591_ENABLE_AIEN | LightSensor.TSL2591_ENABLE_NPIEN])
      print("enable: ", msg)
      self.__i2c.writeto(self.__id, msg)
  def disable (self):
      msg = bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_ENABLE, LightSensor.TSL2591_ENABLE_POWEROFF])
      self.__i2c.writeto(self.__id, msg)
  def setTiming (self, value):
      self.__integration = value
      msg = bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_CONTROL, self.__integration | self.__gain])
      self.__i2c.writeto(self.__id, msg)
  def setGain (self, value):
      self.__gain = value
      msg = bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_CONTROL, self.__integration | self.__gain])
      self.__i2c.writeto(self.__id, msg)
  def calculateLux(self, full, ir):
      # Check for overflow conditions first
      if (full == 0xFFFF) | (ir == 0xFFFF):
        return 0
      case_integ = {
            LightSensor.TSL2591_INTEGRATIONTIME_100MS: 100.0,
            LightSensor.TSL2591_INTEGRATIONTIME_200MS: 200.0,
            LightSensor.TSL2591_INTEGRATIONTIME_300MS: 300.0,
            LightSensor.TSL2591_INTEGRATIONTIME_400MS: 400.0,
            LightSensor.TSL2591_INTEGRATIONTIME_500MS: 500.0,
            LightSensor.TSL2591_INTEGRATIONTIME_600MS: 600.0,
      }
      if self.__integration in case_integ.keys():
            atime = case_integ[self.__integration]
      else:
            atime = 100.0
      case_gain = {
            LightSensor.TSL2591_GAIN_LOW:    1.0,
            LightSensor.TSL2591_GAIN_MED:   25.0,
            LightSensor.TSL2591_GAIN_HIGH: 428.0,
            LightSensor.TSL2591_GAIN_MAX: 9876.0,
      }
      if self.__gain in case_gain.keys():
            again = case_gain[self.__gain]
      else:
            again = 1.0
      # cpl = (ATIME * AGAIN) / DF
      cpl = (atime * again) / LightSensor.TSL2591_LUX_DF
      lux1 = (full - (LightSensor.TSL2591_LUX_COEFB * ir)) / cpl
      lux2 = ((LightSensor.TSL2591_LUX_COEFC * full) - (LightSensor.TSL2591_LUX_COEFD * ir)) / cpl
      # The highest value is the approximate lux equivalent
      return -1.0 * max([lux1, lux2])
  def getFullLuminosity(self):
      #self.enable()
      time.sleep(0.120*self.__integration+1)  # not sure if we need it "// Wait x ms for ADC to complete"
      self.__i2c.writeto(self.__id, bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_CHAN1_LOW]))
      full = self.__i2c.readfrom(self.__id, 2)
      self.__i2c.writeto(self.__id, bytes([LightSensor.TSL2591_COMMAND_BIT | LightSensor.TSL2591_REGISTER_CHAN0_LOW]))
      ir = self.__i2c.readfrom(self.__id, 2)
      #self.disable()
      vfull = full[0]+(full[1]*256)
      vir = ir[0]+(ir[1]*256)
      return vfull, vir

# bytearray(s)

print("Running...")
from machine import I2C

# configure the I2C bus
i2c = I2C(0, I2C.MASTER, baudrate=25000)
ids = i2c.scan()
print("scan found:", ids)
ls = LightSensor(i2c, ids[0])

# Turn the sensor on
ls.enable()
print("sensor enabled")
ls.setGain(LightSensor.TSL2591_GAIN_MED)
i = 0
while i < 10:
  full, ir = ls.getFullLuminosity()
  print('full=', full, 'ir=', ir)
  print('lux=', ls.calculateLux(full, ir))
  time.sleep(5)
  
ls.disable()
print("finito")


