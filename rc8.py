from time import sleep
import RPi.GPIO as GPIO
import yaml

class raspRobot():

  def setMotorDirection(self, direction, pin_dir_A, pin_dir_B ):
    ''' sets the IO pins to control motor direction
    '''
    GPIO.output( pin_dir_A, direction[0])
    GPIO.output( pin_dir_B, direction[1])

  def __init__( self, params ):
    self._motor_A = self._setupMotorGpio( params['motorA'] )
    self._motor_B = self._setupMotorGpio( params['motorB'] )
    self._speed = 0
    self._speedOffset = 0

  def setSpeed( self, speed ):
    print "speed", speed
    self._speed=speed
    self.updateSpeed()
    return

  def setDirection( self, speedOffset):
    print "new direction:", speedOffset
    self.updateSpeed()
    self._speedOffset=speedOffset
    return

  def updateSpeed( self ):
    self._motor_A.start( self._speed+self._speedOffset)
    self._motor_B.start( self._speed-self._speedOffset)
    return

  def _setupMotorGpio( self, params ):
      ''' Sets parameters for the IOs
          params: an object with the following properties
          params.dir_A: motor direction pin A
          params.dir_B: motor direction pin b
          params.pwm: pin to output PWM signals to (for speed)
          params.freq: frequency for PWM signal
          returns the motor object
      '''

      # set the pin numbering scheme
      GPIO.setmode(GPIO.BCM)
      # set pin for output
      GPIO.setup( params["dir_A"], GPIO.OUT )
      GPIO.setup( params["dir_B"], GPIO.OUT )
      GPIO.setup( params["pwm"], GPIO.OUT )
      motor = GPIO.PWM( params["pwm"], params["freq"] )

      self.setMotorDirection( (0,1), params['dir_A'], params['dir_B'] )

      return motor

class rc8():
  def __init__( self, robot ):
    self._robot = robot

  def runLoop( self, count ):
    loopCount = 0

    speed = 50
    dirOffset = 30

    self._robot.setSpeed( 50 )

    while( loopCount < count ):
      self._robot.setDirection( dirOffset )
      sleep( 1 )
      self._robot.setDirection( 0 )
      sleep( 2 )
      self._robot.setDirection( -1*dirOffset )
      sleep( 1 )
      self._robot.setDirection( 0 )
      sleep( 2 )

      loopCount = loopCount +1

def readConfig( filename ):
  with open("config.yaml", 'r') as stream:
    try:
        params = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

    return params

if __name__ == "__main__":
  params = readConfig('config.yaml')

  robot = raspRobot( params )
  rc = rc8( robot )
  rc.runLoop( 10 )