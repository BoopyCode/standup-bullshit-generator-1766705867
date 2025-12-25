#!/usr/bin/env python3
"""
Standup Bullshit Generator - Because actual work is overrated.
"""

import random
import sys

def generate_standup_update():
    """
    Generates a perfectly plausible standup update with zero actual content.
    The secret sauce: vague verbs + technical buzzwords + non-committal timelines.
    """
    
    # Building blocks of corporate nonsense
    verbs = ["refactoring", "optimizing", "investigating", "debugging", "syncing", 
             "aligning", "streamlining", "modularizing", "containerizing"]
    
    nouns = ["legacy code", "tech debt", "performance issues", "edge cases", 
             "integration points", "data pipeline", "API layer", "microservices"]
    
    blockers = ["waiting on PR review", "blocked by dependencies", "environment issues",
                "clarification needed", "meeting conflicts", "CI/CD pipeline down"]
    
    plans = ["continue with", "finalize", "wrap up", "move forward with", 
             "pivot to", "deep dive into", "spike on"]
    
    # Yesterday: I was doing something vague
    yesterday = f"Yesterday I was {random.choice(verbs)} the {random.choice(nouns)}."
    
    # Today: I will continue doing something equally vague
    today = f"Today I'll {random.choice(plans)} the {random.choice(nouns)}."
    
    # Blockers: Always have one, but make it sound reasonable
    blocker = f"Blocked by: {random.choice(blockers)}."
    
    # 30% chance of sounding extra productive
    if random.random() < 0.3:
        extra = "Also did some pair programming and knowledge sharing."
        return f"{yesterday} {extra}\n{today}\n{blocker}"
    
    return f"{yesterday}\n{today}\n{blocker}"

def main():
    """
    Main function - because every script needs one, apparently.
    """
    print("\n=== STANDUP BULLSHIT GENERATOR ===\n")
    print("Your perfectly plausible standup update:\n")
    print(generate_standup_update())
    print("\nRemember: If it sounds technical, it must be progress!\n")

if __name__ == "__main__":
    main()