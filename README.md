# nth_py
Return or exclude the `nth` lines supplied from stdin as output on stdout. See the Rust version of this utility here: [nth_rs](https://github.com/alexdelorenzo/nth_rs).

# Install

```bash
pip3 install nth_py
```

# Usage

```bash
$ dmesg | nth 0 1 2 3
[    4.095065] xhci-hcd xhci-hcd.3.auto: xHCI Host Controller
[    4.100328] xhci-hcd xhci-hcd.3.auto: new USB bus registered, assigned bus number 4
[    4.107985] xhci-hcd xhci-hcd.3.auto: Host supports USB 3.0  SuperSpeed
[    4.109677] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 52000000Hz, actual 50000000HZ div = 0)

```

To better illustrate, let's enumerate each line of stdin:

```bash
$ dmesg | count | nth 0 1 2 3
     0  [    4.095065] xhci-hcd xhci-hcd.3.auto: xHCI Host Controller
     1  [    4.100328] xhci-hcd xhci-hcd.3.auto: new USB bus registered, assigned bus number 4
     2  [    4.107985] xhci-hcd xhci-hcd.3.auto: Host supports USB 3.0  SuperSpeed
     3  [    4.109677] mmc_host mmc0: Bus speed (slot 0) = 50000000Hz (slot req 52000000Hz, actual 50000000HZ div = 0)
```

# License
See `LICENSE`. If you'd like to use this project with a different license, please get in touch.
