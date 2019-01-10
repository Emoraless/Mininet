import sys
from mininet.node import Node
from mininet.topo import Topo
from mininet.link import TCLink
from mininet.node import Controller, RemoteController, CPULimitedHost

class MyTopo ( Topo ):
    "Simple topology example."
    
    def __init__( self ):
        "Create custom topo"
        
        # Initialize topology
        Topo.__init__( self )
        
        S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
        S3 = self.addSwitch( 's3' )
        S4 = self.addSwitch( 's4' )
        S5 = self.addSwitch( 's5' )
        S6 = self.addSwitch( 's6' )
        S7 = self.addSwitch( 's7' )
        S8 = self.addSwitch( 's8' )
        S9 = self.addSwitch( 's9' )
        S10 = self.addSwitch( 's10' )
        S11 = self.addSwitch( 's11' )
        S12 = self.addSwitch( 's12' )
        
        # Add hosts and switches
        H1 = self.addHost( 'h1', ip='10.0.0.1/8', mac='00.00.00.00.00.01', port=1010 )
        H2 = self.addHost( 'h2', ip='10.0.0.2/8', mac='00.00.00.00.00.02', port=2020 )
        H3 = self.addHost( 'h3', ip='10.0.0.3/8', mac='00.00.00.00.00.03', port=3030 )
        H4 = self.addHost( 'h4', ip='10.0.0.4/8', mac='00.00.00.00.00.04', port=4040 )
        H5 = self.addHost( 'h5', ip='10.0.0.5/8', mac='00.00.00.00.00.05', port=5050 )
        H6 = self.addHost( 'h6', ip='10.0.0.6/8', mac='00.00.00.00.00.06', port=6060 )
        H7 = self.addHost( 'h7', ip='10.0.0.7/8', mac='00.00.00.00.00.07', port=7070 )
        H8 = self.addHost( 'h8', ip='10.0.0.8/8', mac='00.00.00.00.00.08', port=8080 )
        H9 = self.addHost( 'h9', ip='10.0.0.9/8', mac='00.00.00.00.00.09', port=9090 )
        H10 = self.addHost( 'h10', ip='10.0.0.10/8', mac='00.00.00.00.00.10', port=1111 )
        H11 = self.addHost( 'h11', ip='10.0.0.11/8', mac='00.00.00.00.00.11', port=1212 )
        H12 = self.addHost( 'h12', ip='10.0.0.12/8', mac='00.00.00.00.00.12', port=1313 )
        
        # Add links
        self.addLink( H1, S1, bw=2, delay='3ms', max_queue_size=1000, loss=1 )
        self.addLink( H2, S2 )
        self.addLink( H3, S3 )
        self.addLink( H4, S4 )
        self.addLink( H5, S5 )
        self.addLink( H6, S6 )
        self.addLink( H7, S7 )
        self.addLink( H8, S8 )
        self.addLink( H9, S9 )
        self.addLink( H10, S10 )
        self.addLink( H11, S11 )
        self.addLink( H12, S12 )
        
        # A - B - C - D
        self.addLink( S1, S2 )
        self.addLink( S1, S3 )
        self.addLink( S1, S4 )
        self.addLink( S2, S3 )
        self.addLink( S2, S4 )
        self.addLink( S2, S5 )
        self.addLink( S3, S4, bw=2, delay='3ms', max_queue_size=1000, loss=1 )
        
        # E - F - G
        self.addLink( S5, S6 )
        self.addLink( S6, S7 )
        self.addLink( S7, S5 )
        # G - I - H - J
        self.addLink( S7, S8 )
        self.addLink( S7, S9 )
        self.addLink( S7, S10 )
        self.addLink( S8 ,S9 )
        self.addLink( S8, S10)
        self.addLink( S9, S10, bw=2, delay='3ms', max_queue_size=1000, loss=1 )
        # F - K - L
        self.addLink( S6, S11 )
        self.addLink( S11, S12 )
        self.addLink( S12, S6 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
