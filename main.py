#!/usr/bin/env python

from flask import Flask, render_template, url_for
import random

app = Flask(__name__)

@app.route("/")
def roll():
  rolls = [random.choice(["-","0","+"]) for i in range(4)]
  score = len([i for i in rolls if i == "+"]) - len([i for i in rolls if i == "-"])
  if score > 0:
    score = "+" + str(score)
  else:
    score = str(score)

  return render_template("roll.html", rolls=rolls, score=score)

if __name__ == "__main__":
  app.run()
