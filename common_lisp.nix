{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = with pkgs; [
    roswell
    (sbcl.withPackages (s:
      with s; [
        md5
        youtube
        quicklisp-starter
      ]))
  ];
  shellHook = ''
    echo "Welcome to Common Lisp dev shell"
    sbcl --version
    ros --version
    ros setup
    ros run --eval '(ql:quickload :swank)'  --eval '(swank:create-server :dont-close t)'
  '';
}
