void deal_data(String data) {
  Serial.println(data);
  if (data[0] == 'P' and data[5] == 'P') {
    if (data[1] == 'H') {
      Serial.println("Yes");
      digitalWrite(lightPin, HIGH);
    } else if (data[1] == 'L') {
      digitalWrite(lightPin, LOW);
      Serial.println("No");
    }
  }
}

