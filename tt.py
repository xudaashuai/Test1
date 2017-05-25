#!/usr/bin/python

"clusterdemo.py: demo of Mininet Cluster Edition prototype"
from mininet.node import RemoteController, OVSSwitch
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink

# ^ Could also use: RemoteSSHLink, RemoteGRELink
from mininet.topolib import TreeTopo
from mininet.log import setLogLevel

from mininet.topo import Topo


class MTopo(Topo):
    "Simple topology example."

    def build(self):
        "Create custom topo."

        # Initialize topology
        # Add hosts and switches
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        a1 = self.addSwitch('a1')
        a2 = self.addSwitch('a2')
        a3 = self.addSwitch('a3')
        a4 = self.addSwitch('a4')
        e1 = self.addSwitch('e1')
        e2 = self.addSwitch('e2')
        e3 = self.addSwitch('e3')
        e4 = self.addSwitch('e4')
        # Add links
        self.addLink(s1, s2)
        self.addLink(a1, s1)
        self.addLink(a1, s2)
        self.addLink(a2, s1)
        self.addLink(a2, s2)
        self.addLink(a3, s1)
        self.addLink(a3, s2)
        self.addLink(a4, s1)
        self.addLink(a4, s2)
        self.addLink(a3, e3)
        self.addLink(a3, e4)
        self.addLink(a4, e3)
        self.addLink(a4, e4)
        self.addLink(h1, e1)
        self.addLink(h2, e1)
        self.addLink(h5, e3)
        self.addLink(h7, e4)
        self.addLink(h6, e3)
        self.addLink(h8, e4)
        self.addLink(h1, e1)
        self.addLink(h2, e1)
        self.addLink(h3, e2)
        self.addLink(h4, e2)
        self.addLink(a1, e1)
        self.addLink(a1, e2)
        self.addLink(a2, e1)
        self.addLink(a2, e2)


class MMTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1', ip='127.1.0.0/16')
        s2 = self.addSwitch('s2', ip='127.2.0.0/16')
        s3 = self.addSwitch('s3', ip='127.1.0.1')
        s4 = self.addSwitch('s4', ip='127.1.0.2')
        s5 = self.addSwitch('s5', ip='127.2.0.1')
        s6 = self.addSwitch('s6', ip='127.2.0.2')
        s7 = self.addSwitch('s7', ip='127.1.1.0/24')
        s8 = self.addSwitch('s8', ip='127.1.2.0/24')
        s9 = self.addSwitch('s9', ip='127.2.1.0/24')
        s10 = self.addSwitch('s10', ip='127.2.2.0/24')

        h1 = self.addHost('h1', ip='10.0.0.1')
        h2 = self.addHost('h2', ip='10.0.0.2')
        h3 = self.addHost('h3', ip='20.0.0.1')
        h4 = self.addHost('h4', ip='20.0.0.2')
        h5 = self.addHost('h5', ip='30.0.0.1')
        h6 = self.addHost('h6', ip='30.0.0.2')
        h7 = self.addHost('h7', ip='40.0.0.1')
        h8 = self.addHost('h8', ip='40.0.0.2')
        # Add links
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s2, s5)
        self.addLink(s2, s6)
        self.addLink(s7, s3)
        self.addLink(s8, s4)
        self.addLink(s7, s4)
        self.addLink(s8, s3)
        self.addLink(s9, s5)
        self.addLink(s10, s6)
        self.addLink(s9, s6)
        self.addLink(s10, s5)
        self.addLink(s7, h1)
        self.addLink(s8, h3)
        self.addLink(s7, h2)
        self.addLink(s8, h4)
        self.addLink(s9, h5)
        self.addLink(s10, h7)
        self.addLink(s9, h6)
        self.addLink(s10, h8)
topos = { 'mytopo': ( lambda: MMTopo() ) }

def demo():
    net = Mininet(topo=MMTopo(), cleanup=True, link=TCLink,
                  autoSetMacs=True, autoStaticArp=True,
                  switch=OVSSwitch
                  )
    net.start()
    #cli = CLI(net,script='b.txt')
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    demo()
