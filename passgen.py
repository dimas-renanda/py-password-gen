#!/usr/bin/env python3
"""Secure password generator."""
import secrets, string, argparse

def generate(length=16, use_symbols=True, use_digits=True, use_upper=True):
    chars = string.ascii_lowercase
    if use_upper:   chars += string.ascii_uppercase
    if use_digits:  chars += string.digits
    if use_symbols: chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"
    while True:
        pwd = ''.join(secrets.choice(chars) for _ in range(length))
        if use_upper and not any(c.isupper() for c in pwd): continue
        if use_digits and not any(c.isdigit() for c in pwd): continue
        if use_symbols and not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in pwd): continue
        return pwd

p = argparse.ArgumentParser()
p.add_argument("--length","-l",type=int,default=16)
p.add_argument("--count","-c",type=int,default=1)
p.add_argument("--no-symbols",action="store_true")
p.add_argument("--no-digits",action="store_true")
p.add_argument("--no-upper",action="store_true")
args = p.parse_args()

for i in range(args.count):
    pwd = generate(args.length, not args.no_symbols, not args.no_digits, not args.no_upper)
    strength = "🔴 Weak" if args.length < 8 else "🟡 Medium" if args.length < 16 else "🟢 Strong"
    print(f"{pwd}  {strength}")
