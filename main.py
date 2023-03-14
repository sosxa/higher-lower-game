import art
import data
from art import logo
from art import vs
from data import data
import random

score = 0
celeb_a = None
celeb_b = None
on = True


def first_celeb():
    print(logo)
    global celeb_a
    celeb_a = random.choice(data)
    print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}")


def second_celeb():
    print(vs)
    global celeb_b
    celeb_b = random.choice(data)
    print(f"Against B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")


def compare(celeb_a, celeb_b):
    global score
    global on
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == "A" and celeb_a['follower_count'] >= celeb_b['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    elif guess == "B" and celeb_b['follower_count'] >= celeb_a['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        on = False
        return print(f"Sorry, that's wrong. Final score: {score}")


while on:
    first_celeb()
    second_celeb()
    compare(celeb_a, celeb_b)
