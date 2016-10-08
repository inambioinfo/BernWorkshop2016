#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os, sys, re
import logging
import argparse
import subprocess

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)



def main():

    parser = argparse.ArgumentParser(description="instantiate user spaces", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--ip_addr", type=str, required=True, help="IP address for server")
    parser.add_argument("--attendee_list", type=str, required=True, help="attendee list file")
    parser.add_argument("--apache_base_port", type=int, default=8001, help="base port for apache")
    parser.add_argument("--gateone_base_port", type=int, default=9001, help="base port for gateone")
    
    args = parser.parse_args()

    
    apache_user_port = args.apache_base_port
    gateone_user_port = args.gateone_base_port
    
    print("<html><body><h1>Trinity RNA-Seq Workshop in Bern, Switzerland (October 10-11, 2016)</h1></body></html>")

    print("<style>\n" +
          "tr:nth-child(even) {background: #CCC}\n" +
          "tr:nth-child(odd) {background: #FFF}\n" +
          "</style>\n")
    

    print("<table shade='rows'>\n")
    print ("<tr><th>id</th><th>Attendee</th><th>SSH Terminal</th><th>Apache Viewer</th></tr>")
    
    user_id = 1
    with open(args.attendee_list) as f:
        for attendee_name in f:
            attendee_name = attendee_name.rstrip()
            print("<tr><td>{}</td>".format(user_id) +
                  "<td>{}</td>".format(attendee_name) +
                  "<td><a href=\"{}\" target='sshterm'>ssh terminal</a></td>".format(url_maker(args.ip_addr, gateone_user_port)) +
                  "<td><a href=\"{}\" target='apacheview'>apache</a></td>".format(url_maker(args.ip_addr, apache_user_port)) +
                  "</tr>")
            
            apache_user_port += 1
            gateone_user_port += 1
            user_id += 1

    print("</table></body></html>")
    
    sys.exit(0)


def url_maker(ip_addr, port_num):

    return("http://" + ip_addr + ":" + str(port_num))



####################
 
if __name__ == "__main__":
    main()