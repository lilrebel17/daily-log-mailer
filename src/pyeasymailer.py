#!/usr/bin/env python

from sub_commands.setup import subcommand as setup
import argparse

arg_parser = argparse.ArgumentParser(prog='pyeasymailer',description='Quickly setup and send non-html emails using a remote SMTP like gmail or ZoHo',)

sub_parser = arg_parser.add_subparsers()

setup_parser = sub_parser.add_parser('setup',help='Runs the interactive setup for pyeasymailer. Can be used to set the default settings used to email.')
setup_parser.set_defaults(function=setup.start_default_settings_interactive_setup())

args = arg_parser.parse_args()
