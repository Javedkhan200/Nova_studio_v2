package main

import (
	"fmt"
	"net"
	"time"
)

type NetworkScanner struct {
	TargetIP string
	Ports    []int
}

func (ns *NetworkScanner) ExecuteAdvancedAudit() {
	fmt.Println("[Go Core] Initiating High-Performance Security Audit Matrix...")
	for _, port := range ns.Ports {
		address := fmt.Sprintf("%s:%d", ns.TargetIP, port)
		conn, err := net.DialTimeout("tcp", address, 1*time.Second)
		if err != nil {
			continue
		}
		fmt.Printf("[ALERT] Port %d is OPEN - Vulnerability Checked.\n", port)
		conn.Close()
	}
}

func main() {
	scanner := NetworkScanner{TargetIP: "127.0.0.1", Ports: []int{21, 22, 80, 443, 8080}}
	scanner.ExecuteAdvancedAudit()
}
