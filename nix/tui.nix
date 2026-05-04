# nix/tui.nix — Gengar TUI (Ink/React) compiled with tsc and bundled
{ pkgs, hermesNpmLib, ... }:
let
  src = ../ui-tui;
  npmDeps = pkgs.fetchNpmDeps {
    inherit src;
    hash = "sha256-a/HGI9OgVcTnZrMXA7xFMGnFoVxyHe95fulVz+WNYB0=";
  };

  npm = hermesNpmLib.mkNpmPassthru { folder = "ui-tui"; attr = "tui"; pname = "gengar-tui"; };

  packageJson = builtins.fromJSON (builtins.readFile (src + "/package.json"));
  version = packageJson.version;
in
pkgs.buildNpmPackage (npm // {
  pname = "gengar-tui";
  inherit src npmDeps version;

  doCheck = false;
  npmFlags = [ "--legacy-peer-deps" ];

  installPhase = ''
    runHook preInstall

    mkdir -p $out/lib/gengar-tui

    cp -r dist $out/lib/gengar-tui/dist

    # runtime node_modules
    cp -r node_modules $out/lib/gengar-tui/node_modules

    # @gengar/ink is a file: dependency, we need to copy it in fr
    rm -f $out/lib/gengar-tui/node_modules/@gengar/ink
    cp -r packages/gengar-ink $out/lib/gengar-tui/node_modules/@gengar/ink

    # package.json needed for "type": "module" resolution
    cp package.json $out/lib/gengar-tui/

    runHook postInstall
  '';
})
