#!/usr/bin/env ruby
# A Ruby script that accepts one argument and pass it to a regular expression
puts ARGV[0].scan(/School/).join
