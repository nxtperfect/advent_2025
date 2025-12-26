{}: let
  rustOverlay = import (builtins.fetchTarball "https://github.com/oxalica/rust-overlay/archive/master.tar.gz");
  pkgs = import <nixpkgs> {overlays = [rustOverlay];};
in
  pkgs.mkShell {
    buildInputs = with pkgs; [
      python312
      python312Packages.numpy
    ];
    shellHook = ''
      echo "Welcome to AoC dev shell"
    '';
  }
