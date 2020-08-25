---
layout: post
title:  "BEAGLE Installation"
date:   2020-08-25
categories: mocks
---

I plan on using <a href="http://www.jacopochevallard.org/beagle/">BEAGLE</a> to create a "parent catalog" of SEDs.

## Installation

Ryan very kindly gave me instructions on how to install BEAGLE. Here are his instructions:

1. <a href="https://docs.docker.com/docker-for-mac/install/#:~:text=Install%20and%20run%20Docker%20Desktop%20on%20Mac.%201,verify%20that%20you%20have%20the%20latest%20version.%20">Install Docker</a>

2. Get the beagle images: docker pull beagletool/beagle:0.24.4

3. Run beagle by running its docker container: docker run beagletool/beagle:0.24.4 ARGS

4. You can think of "docker run beagletool/beagle:0.24.4" being equivalent to a command called beagle. For example, running "docker run beagletool/beagle:0.24.4 --help" will return the help menu from beagle.

This worked perfectly.

## Running BEAGLE

From the help menu. the usage is:

<code>BEAGLE  --parameter-file value [--fit] [--mock] [--test-speed] [--n-test value] [--profiling] [--help] [--version]</code>

I will want to create a mock catalog, but I need to figure out how the parameter file should be formatted...

Table 2 in their paper lists all the adjustable parameters, but I can't find a description or example of a paramter file anywhere. Need to check with Brant if he has any ideas, or contact the authors (though I think they left the field?).
