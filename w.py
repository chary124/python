def test(i,face,x,key,stu,ts):
    showID = x.bssid if len(x.ssid)==0 or x.ssid=='\\x00' or len(x.ssid)>len(x.bssid) else x.ssid
    key_index = 0
    while key_index < len(key):
        k = key[key_index]
        x.key = k.strip()
        face.remove_all_network_profiles()
        profile = Profile()
        profile.ssid = x.ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = x.key
        face.connect(face.add_network_profile(profile))
        code = -1
        t1 = time.time()
        now = time.time() - t1
        while True:
            time.sleep(0.1)
            code = face.status()
            now = time.time()-t1
            if now>ts:
                break
            stu.write("\r%-6s| %-18s| %5.2fs | %-6s %-15s | %-12s"%(i,showID,now,len(key)-key_index,k.strip(),get_iface_status(code)))
            stu.flush()
            if code == const.IFACE_DISCONNECTED :
                break
            elif code == const.IFACE_CONNECTED:
                face.disconnect()
                stu.write("\r%-6s| %-18s| %5.2fs | %-6s %-15s | %-12s\n%")p
                