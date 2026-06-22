package main
import (
    "fmt"
    "net"
    "time"
)
func scanPort(protocol, hostname string, port int) bool {
    address := fmt.Sprintf("%s:%d", hostname, port)
    conn, err := net.DialTimeout(protocol, address, 2*time.Second)
    if err != nil { return false }
    defer conn.Close()
    return true
}
func main() {
    fmt.Println("Nova Go Engine: Network Matrix Ready for Hacking & Defense.")
}
