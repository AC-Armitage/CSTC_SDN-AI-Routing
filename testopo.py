from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel

def SetUp():
    hosts = {}
    ovss = {}
    edge_ovs = {}
    net = Mininet(controller=Controller)
    net.addController()
    for i in range(1, 13):
        hosts[f"h{i}"] = net.addHost(f"h{i}")
    for i in range(1, 7):
        ovss[f"s{i}"] = net.addSwitch(f"s{i}")
    for i in range(1, 5):
        edge_ovs[f"e_s{i}"] = net.addSwitch(f"e_s{i}")
    return net, hosts, ovss, edge_ovs

def Linkup(net, hosts, ovss, edge_ovs):
    for i in range(1, 4):
        net.addLink(hosts[f"h{i}"], ovss[f"s1"])
    for i in range(4, 7):
        net.addLink(hosts[f"h{i}"], ovss[f"s2"])
    net.addLink(ovss[f"s1"], edge_ovs[f"e_s1"])
    net.addLink(ovss[f"s2"], edge_ovs[f"e_s1"])
    net.addLink(edge_ovs[f"e_s1"], edge_ovs[f"e_s2"])
    net.addLink(edge_ovs[f"e_s2"], ovss[f"s5"])
    net.addLink(ovss[f"s5"], edge_ovs[f"e_s3"])
    net.addLink(ovss[f"s5"], edge_ovs[f"e_s4"])
    net.addLink(edge_ovs[f"e_s3"], ovss[f"s3"])
    net.addLink(edge_ovs[f"e_s4"], ovss[f"s4"])
    for i in range(7, 9):
        net.addLink(hosts[f"h{i}"], ovss[f"s3"])
    for i in range(9, 11):
        net.addLink(hosts[f"h{i}"], ovss[f"s4"])
    net.addLink(ovss[f"s5"], edge_ovs[f"e_s2"])
    net.addLink(edge_ovs[f"e_s2"], ovss[f"s6"])
    for i in range(11, 13):
        net.addLink(hosts[f"h{i}"], ovss[f"s6"])

if __name__ == '__main__':
    setLogLevel('info')
    net, hosts, ovss, edge_ovs = SetUp()
    Linkup(net, hosts, ovss, edge_ovs)
    net.start()
    CLI(net)
    net.stop()
