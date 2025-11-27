{ config, pkgs, ... }:
{
  imports = [
    ./hardware-configuration.nix
  ];

  networking.hostName = "shtirlitz";

  services.openssh = {
    enable = true;
    settings = {
      PermitRootLogin = "prohibit-password";
      PasswordAuthentication = false;
    };
  };

  nix.settings.experimental-features = [ "nix-command" "flakes" ];

  users.users = {
    root = {
      openssh.authorizedKeys.keys = [
        ''ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG/6GNBs/+NewQ6AK4igl7dZp8+HgCUzl++eIBV/3TGk terow-rist@nixos''
      ];
    };
  };

  environment.systemPackages = with pkgs; [
    helix
    git
  ];

  system.stateVersion = "25.05"; #change it!
}
