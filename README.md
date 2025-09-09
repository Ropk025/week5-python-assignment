# Week 5 Python Assignment – Classes & Polymorphism

This repository contains solutions for Week 5 of the Power Learn Project Python course. It includes two activities focused on object-oriented programming concepts: class design, inheritance, and polymorphism.

---

## 🧱 Assignment 1: Superhero Class

A custom class `Superhero` was created to represent fictional heroes. It includes:

- **Attributes**: `name`, `power`, and `origin`
- **Methods**:
  - `introduce()` – prints a brief intro of the hero
  - `use_power()` – describes how the hero uses their power

### Inheritance
Two subclasses extend the base class:
- `FlyingHero` – adds `flight_speed` and overrides `use_power()`
- `TechHero` – adds `gadget` and overrides `use_power()`

This demonstrates **encapsulation** and **polymorphism** through method overriding.

---

## 🎭 Activity 2: Polymorphism Challenge

Three vehicle classes (`Car`, `Plane`, `Boat`) inherit from a base class `Vehicle`. Each class overrides the `move()` method to reflect its unique behavior:

- `Car.move()` → "Driving 🚗"
- `Plane.move()` → "Flying ✈️"
- `Boat.move()` → "Sailing 🚤"

This showcases **polymorphism** by allowing different objects to respond to the same method in distinct ways.

---

## 🧪 How to Run

Make sure you have Python installed. Then run:

```bash
python week5_assignment.py