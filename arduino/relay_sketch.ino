void setup(){
  Serial.begin(9600);

  //Set all the pins we need to output pins
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop (){
  if (Serial.available()) {
      //read serial as ascii integer
      int ser = Serial.read();
      //Print the value in the serial monitor
      Serial.println(ser);

      // 0  :: Pin2   :: On
      if( ser == 48 ){
        digitalWrite( 2, HIGH );
      }
      // 1  :: Pin2   :: Off
      if( ser == 49 ){
        digitalWrite( 2, LOW );
      }
      // 0  :: Pin3   :: On
      if( ser == 50 ){
        digitalWrite( 3, HIGH );
      }
      // 1  :: Pin3   :: Off
      if( ser == 51 ){
        digitalWrite( 3, LOW );
      }
  }

}