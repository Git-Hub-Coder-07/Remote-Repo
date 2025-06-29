import subprocess

def get_wifi_passwords():
    try:
        # Get the list of Wi-Fi profiles
        profiles_output = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            shell=True, text=True
        )
        
        # Extract profile names
        profiles = []
        for line in profiles_output.splitlines():
            if "All User Profile" in line:
                profile_name = line.split(":")[1].strip()
                profiles.append(profile_name)

        # Fetch passwords for each profile
        passwords = {}
        for profile in profiles:
            try:
                profile_output = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                    shell=True, text=True
                )
                for line in profile_output.splitlines():
                    if "Key Content" in line:
                        password = line.split(":")[1].strip()
                        passwords[profile] = password
                        break
                else:
                    passwords[profile] = "No password set or not accessible"
            except subprocess.CalledProcessError:
                passwords[profile] = "Error accessing profile details"

        return passwords

    except Exception as e:
        return {"Error": str(e)}

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    for profile, password in wifi_passwords.items():
        print(f"Wi-Fi Name: {profile} | Password: {password}")
