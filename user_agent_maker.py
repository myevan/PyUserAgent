import platform

class UserAgentMaker:
    @classmethod
    def load_os_info(cls):
        def load_linux_pretty_name():
            with open('/etc/os-release') as os_rel_file:
                lines = os_rel_file.read().splitlines()
                for line in lines:
                    assign_idx = line.find('=')
                    if assign_idx >= 0:
                        key = line[:assign_idx]
                        val = line[assign_idx + 1:]
                        if key == 'PRETTY_NAME':
                            if val[0] == '"':
                                return val[1:-1]


        platform_system = platform.system()
        if platform_system == 'Windows':
            win32_ver = platform.win32_ver()
            platform_version = platform.version()
            return ' '.join((platform_system, win32_ver[0], '[' + platform_version + ']'))
        elif platform_system == 'Linux':
            pretty_name = load_linux_pretty_name()
            return ' '.join((platform_system, pretty_name))
        else:
            platform_version = platform.version()
            return ' '.join((platform_system, platform_version))

if __name__ == '__main__':
    print(UserAgentMaker.load_os_info())