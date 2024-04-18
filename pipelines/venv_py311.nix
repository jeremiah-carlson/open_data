{ pkgs ? import <nixpkgs> { } }:

let
  pythonEnv = pkgs.python311.withPackages(ps: [ ]);

in
pkgs.mkShell {
  packages = [
    pythonEnv
  ];

  shellHook=''
  python -m venv venv
  exit
  '';
}