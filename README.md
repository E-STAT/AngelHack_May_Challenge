# AngelHack_May_Challenge

## First Challenge
* **Question**

    John was visiting a friend one day who lived in an apartment, but the instructions that he
    received were a bit confusing. When he arrives, he starts on the ground floor (floor 0) and
    has to follow the instructions one character at a time.
    A left arrow (<) means going up one floor, and a right arrow (>) means going down one floor.
    For example:
    <<>> results in Floor 0, because he goes up twice (<<) and then goes down twice (>>).
    <><> results in Floor 0 as well because he goes up once, followed by down once
    <<< results in Floor 3
    >><<<>> results in Floor -1
    This is what John saw:
    <<<<<<><><><><<<<><><><><><<<<><><><><><>>>><<><><><><><><><><>>>><<<<
    <><><><><><<<<<><><><><><><<<<><><><><><><><><><><><<<<<<><><<><><>>><
    <>><<><<>><><<><><><><><><><<<<<<<<<>><<><><<<><><><><<<<<<>>>>>>>>>>>
    <>><><><>><<<><><><><<><><<><><><><><><><<<<><><><>><<>>>>><><><>><<<>
    <><><><><><>><><><><><><><><><><><><><><><><><<<><><><><><><><><><><><
    ><><><><><><>>>><><><><><><><><><>><<<<<<<<<<>>>>><<<<<>>>><<<<>><<><<
    ><><><><><><><><><><<<<<<<><><<><<><<><<><><><><><<>><><>><><><><><<><
    <<<<>><<<<><><<<><>>><<><>>>>><>>><<><<><><><><<>><><><><><><><><><><>
    <><><><><><<<<><><<<<><<<>>>>>>>>><<><<<>>>>><<<<<<<<<>>>><<><>><><<><
    <>><<>><<>><
    Which floor did he end up on?

* **Answer**

![image](https://user-images.githubusercontent.com/54026058/236300882-84ee1cce-02e9-4dad-91b0-b7119f411689.png)

    John is on the 56th floor


# Second Challenge

* **Question** 
    Run run run away! A group of friends wanted to know who is the fastest amongst them, and
    decided to hold a running race.
    It wasn’t fun just running, so they decided to go for a marathon. These guys are good, but
    must rest occasionally to recover their energy.
    Did I mention that these people are weird? They can only be running (always at their top
    speed), or resting (not moving at all), and can only spend integer amounts of time in either
    state.
    Example case:
    John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
    James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
    After one second (T=1), John has gone 10m, while James has gone 8m. After 6 seconds
    (T=6), John has gone 60m, while James has gone 48m. On the 7th second, John begins
    resting (staying at 60m), while James continues on for a total distance of 64m. On the 9th
    second, both runners are resting. They continue to rest until the 27th second when John
    runs for another 6 seconds. On the 34th second, James runs for another 8 seconds.
    At the 100th second, John is resting after running 240m while James has travelled 200m. In
    this case, John would have won if the race ended at 100 seconds.
    Here are the descriptions of this group of friends:
    1) John can run 10 m/s for 6 seconds, but then must rest for 20 seconds
    2) James can run 8 m/s for 8 seconds, but then must rest for 25 seconds
    3) Jenna can run 12 m/s for 5 seconds, but then must rest for 16 seconds
    4) Josh can run 7 m/s for 7 seconds, but then must rest for 23 seconds
    5) Jacob can run 9 m/s for 4 seconds, but then must rest for 32 seconds
    6) Jerry can run 5 m/s for 9 seconds, but then must rest for 18 seconds
    After 1234 seconds, what is the distance of the winning runner?

* **Answer** 

    ![image](https://ray.so/#language=python&code=ZGVmIGZhc3Rlc3RfcnVubmVyKHNwZWVkOiBpbnQsIGxpbWl0OiBpbnQsIHJlc3Q6IGludCkgLT4gaW50OgogICAgIiIiCiAgICBDYWxjdWxhdGVzIHRoZSB0b3RhbCBkaXN0YW5jZSBjb3ZlcmVkIGJ5IGEgcnVubmVyIGdpdmVuIHRoZWlyCiAgICBydW5uaW5nIHNwZWVkLCBsaW1pdCB0aW1lLCBhbmQgcmVzdCB0aW1lLCBhc3N1bWluZyB0aGV5IHJ1biBmb3IKICAgIGEgdG90YWwgb2YgMTIzNCBzZWNvbmRzLgoKICAgIFBhcmFtZXRlcnM6CiAgICAgICAgc3BlZWQgKGludCk6IFRoZSBzcGVlZCBvZiB0aGUgcnVubmVyIGluIHVuaXRzIHBlciBzZWNvbmQuCiAgICAgICAgbGltaXQgKGludCk6IFRoZSBtYXhpbXVtIHRpbWUgdGhlIHJ1bm5lciBjYW4gcnVuIHdpdGhvdXQgcmVzdGluZy4KICAgICAgICByZXN0IChpbnQpOiBUaGUgdGltZSB0aGUgcnVubmVyIHJlc3RzIGFmdGVyIHJlYWNoaW5nIHRoZWlyIGxpbWl0LgoKICAgIFJldHVybnM6CiAgICAgICAgaW50OiBUaGUgdG90YWwgZGlzdGFuY2UgY292ZXJlZCBieSB0aGUgcnVubmVyIGluIHRoZSBnaXZlbiB0aW1lLgoKICAgIEV4YW1wbGU6CiAgICAgICAgPj4-IGZhc3Rlc3RfcnVubmVyKDEwLCA2LCAyMCkKICAgICAgICA4MjAKICAgICIiIgogICAgZGlzdGFuY2UgPSAwCiAgICB0aW1lX3VzZWQgPSAwCiAgICAKICAgICMgUnVuIGFuZCByZXN0IGluIGEgbG9vcCB1bnRpbCAxMjM0IHNlY29uZHMgYXJlIHVwCiAgICBmb3IgaSBpbiByYW5nZSgxMjM0IC8vIChsaW1pdCArIHJlc3QpKToKICAgICAgICAjIFJ1biBmb3IgdGhlIGxpbWl0IHRpbWUgdW5pdHMKICAgICAgICBkaXN0YW5jZSArPSBzcGVlZCAqIGxpbWl0CiAgICAgICAgdGltZV91c2VkICs9IGxpbWl0CgogICAgICAgICMgUmVzdCBmb3IgdGhlIHJlc3QgdGltZSB1bml0cwogICAgICAgIHRpbWVfdXNlZCArPSByZXN0CgogICAgIyBJZiB0aGVyZSBpcyByZW1haW5pbmcgdGltZSwgcnVuIGZvciB0aGUgcmVtYWluaW5nIHRpbWUKICAgIHJlbWFpbmluZ190aW1lID0gMTIzNCAlIChsaW1pdCArIHJlc3QpCiAgICBpZiByZW1haW5pbmdfdGltZSA-IDA6CiAgICAgICAgaWYgcmVtYWluaW5nX3RpbWUgPD0gbGltaXQ6CiAgICAgICAgICAgIGRpc3RhbmNlICs9IHNwZWVkICogcmVtYWluaW5nX3RpbWUKICAgICAgICBlbHNlOgogICAgICAgICAgICBkaXN0YW5jZSArPSBzcGVlZCAqIGxpbWl0CgogICAgcmV0dXJuIGRpc3RhbmNlCgoKaWYgX19uYW1lX18gPT0gIl9fbWFpbl9fIjoKICAgICMgQ2FsY3VsYXRlIHRoZSBkaXN0YW5jZSBjb3ZlcmVkIGJ5IGVhY2ggcnVubmVyCiAgICBqb2huID0gZmFzdGVzdF9ydW5uZXIoMTAsIDYsIDIwKQogICAgamFtZXMgPSBmYXN0ZXN0X3J1bm5lcig4LCA4LCAyNSkKICAgIGplbm5hID0gZmFzdGVzdF9ydW5uZXIoMTIsIDUsIDE2KQogICAgam9zaCA9IGZhc3Rlc3RfcnVubmVyKDcsIDcsIDIzKQogICAgamFjb2IgPSBmYXN0ZXN0X3J1bm5lcig5LCA0LCAzMikKICAgIGplcnJ5ID0gZmFzdGVzdF9ydW5uZXIoNSwgOSwgMTgpCgogICAgIyBDcmVhdGUgYSBsaXN0IG9mIGRpc3RhbmNlcyBhbmQgZmluZCB0aGUgbWF4aW11bSBkaXN0YW5jZQogICAgd2lubmVyID0gW2pvaG4sIGphbWVzLCBqZW5uYSwgam9zaCwgamFjb2IsIGplcnJ5XQogICAgbWF4X2Rpc3RhbmNlID0gbWF4KHdpbm5lcikKCiAgICAjIFByaW50IHRoZSBtYXhpbXVtIGRpc3RhbmNlIGFuZCB0aGUgaW5kZXggb2YgdGhlIHdpbm5pbmcgcnVubmVyCiAgICBwcmludChmIlRoZSB3aW5uZXIgcmFuIHttYXhfZGlzdGFuY2V9IHVuaXRzISIpCiAgICBwcmludChmIlRoZSB3aW5uaW5nIHJ1bm5lciBpcyAje3dpbm5lci5pbmRleChtYXhfZGlzdGFuY2UpKzF9LiIpCg&theme=candy&background=false&darkMode=true&padding=16)


    The winner is Jenna with 3540m