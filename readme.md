# Testing async requests

This is a test of the guide [here](https://github.com/sagnew?tab=repositories&q=pokemon&type=&language=&sort=)

## Setup env

With git bash or bash or another shell emulation run `install_reqs.sh` (requires conda).

## Run Test script

run script `run_experiments.sh` (assumes conda env `regExp` active)

## Event loop close bug

Initially there was a bug on windows, fix added referencing: [this](https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop)