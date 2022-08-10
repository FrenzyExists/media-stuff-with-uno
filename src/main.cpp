#include <Arduino.h>

#define RED 2
#define BLUE 8
#define WHITE 4
#define WHOTE 7

int redButtonState;
int blueButtonState;
int whiteButtonState;
int whoteButtonState;

int lastRedState = LOW;
int lastBlueState = LOW;
int lastWhiteState = LOW;
int lastWhoteState = LOW;

int whoteCounter = 0;

unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 100;

void setup() {
  pinMode(RED, INPUT);
  pinMode(BLUE, INPUT);
  pinMode(WHITE, INPUT);
  pinMode(WHOTE, INPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of the switch into a local variable:
  int redRead = digitalRead(RED);
  int blueRead = digitalRead(BLUE);
  int whiteRead = digitalRead(WHITE);
  int whoteRead = digitalRead(WHOTE);

  if (redRead != lastRedState || blueRead != lastBlueState || whiteRead != lastWhiteState || whoteRead != lastWhoteState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {

    if (redRead != redButtonState) {
      redButtonState = redRead;

      if (redButtonState == HIGH) {
        switch (whoteCounter) {
        case 0:
          Serial.println("V-UP");
          break;
        case 1:
          Serial.println("B-UP");
          break;
        case 2:
          Serial.println("NEXT");
          break;
        default:
          break;
        }
      }
    } else if (blueRead != blueButtonState) {
      blueButtonState = blueRead;

      if (blueButtonState == HIGH) {
        switch (whoteCounter) {
        case 0:
          Serial.println("V-DOWN");
          break;
        case 1:
          Serial.println("B-DOWN");
          break;
        case 2:
          Serial.println("PREV");
          break;
        default:
          break;
        }
      }
    } else if (whiteRead != whiteButtonState) {
      whiteButtonState = whiteRead;

      if (whiteButtonState == HIGH) {
        switch (whoteCounter) {
        case 0:
          Serial.println("V-MUTE");
          break;
        case 2:
          Serial.println("PLAY");
        default:
          break;
        }
      }
    } else if (whoteRead != whoteButtonState) {
      whoteButtonState = whoteRead;

      if (whoteButtonState == HIGH) {
        whoteCounter = (whoteCounter >= 2) ? 0 : (whoteCounter + 1);
      }
    }
  }

  // save the redRead. Next time through the loop, it'll be the lastRedState:
  lastRedState = redRead;
  lastBlueState = blueRead;
  lastWhiteState = whiteRead;
  lastWhoteState = whoteRead;
}

