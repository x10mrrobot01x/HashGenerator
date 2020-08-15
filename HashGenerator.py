#!/usr/bin/env python3
import argparse, crypt, getpass, random, string, sys, os, colorama

from colorama import Fore, Style

logo = '''\033[1;36;40m
╔═══════════════════════════════════════════════════════════════════════════════════════════════╗
║ ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ║
║ ::▄::█:██::::::▄▄▄▄▄::::▄::█:::::::▄▀::▄███▄::::::▄:::▄███▄:::█▄▄▄▄:██:::::▄▄▄▄▀:████▄:█▄▄▄▄: ║
║ :█:::█:█:█::::█:::::▀▄:█:::█:::::▄▀::::█▀:::▀::::::█::█▀:::▀::█::▄▀:█:█:▀▀▀:█::::█:::█:█::▄▀: ║
║ :██▀▀█:█▄▄█:▄::▀▀▀▀▄:::██▀▀█:::::█:▀▄::██▄▄::::██:::█:██▄▄::::█▀▀▌::█▄▄█::::█::::█:::█:█▀▀▌:: ║
║ :█:::█:█::█::▀▄▄▄▄▀::::█:::█:::::█:::█:█▄:::▄▀:█:█::█:█▄:::▄▀:█::█::█::█:::█:::::▀████:█::█:: ║
║ ::::█:::::█:::::::::::::::█:::::::███::▀███▀:::█::█:█:▀███▀:::::█::::::█::▀::::::::::::::█::: ║
║ :::▀:::::█:::::::::::::::▀:::::::::::::::::::::█:::██::::::::::▀::::::█:::::::::::::::::▀:::: ║
║ ::::::::▀::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::▀::::::::::::::::::::::: ║
╚═════════════════════════════════╗                      ╔══════════════════════════════════════╝
                                  ║  Created by MrRobot  ║
                                  ╚══════════════════════╝
\033[0m'''

def Clear():
    os.system("cls" if os.name == "nt" else "clear")
Clear()

def parse_args():
    parser = argparse.ArgumentParser(description='Generate SHA-512 hash with configurable number of rounds')
    parser.add_argument('--rounds', type=int, help='Number of rounds', default=999999)
    return parser.parse_args()

def create_salt(length):
    rng = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(0, length))

def hash_password(rounds, password):
    salt = create_salt(16)
    password_base = '$6$rounds={rounds}${salt}$'.format(rounds=rounds, salt=salt)
    return crypt.crypt(password, password_base)

def main():
    print(logo)

    args = parse_args()

    password = getpass.getpass()
    verify_password = getpass.getpass(prompt='Verify password')
    if password != verify_password:
        print('\033[1;31mPasswords do not patch.\033[0m', file=sys.stderr)
        sys.exit(1)
    pwdhash = hash_password(rounds=args.rounds, password=password)
    print(pwdhash)

if __name__ == '__main__':
    main()
