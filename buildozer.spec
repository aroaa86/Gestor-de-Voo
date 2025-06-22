[app]

# (str) Title of your application
title = Gestor de voo

# (str) Package name
package.name = gestvoo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (leave empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (list) Include specific patterns (useful to include extra files)
source.include_patterns = requirements.txt

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = kivy==2.2.1,pillow,pyjnius

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API (must be as high as possible)
android.api = 33

# (int) Minimum Android API your app supports
android.minapi = 23

# (int) Android NDK API (should match android.minapi)
android.ndk_api = 23

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (str) Android NDK directory (manual path if needed)
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

# (str) Android SDK directory
android.sdk_path = /usr/local/lib/android/sdk

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (bool) Ignore warnings (useful em builds automáticos)
android.ignore_warnings = 1

# (str) Android entry point (Kivy padrão)
android.entrypoint = org.kivy.android.PythonActivity

# (list) Dynamic libraries a incluir no APK
android.whitelist = lib-dynload/*.so

# (list) Gradle dependencies (exemplo para SQLite JDBC, opcional)
# android.gradle_dependencies = 'org.xerial:sqlite-jdbc:3.36.0'

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Compile options extras
android.add_compile_options = -O3

# (list) Empacotamento - evitar conflitos de bibliotecas em APK
android.add_packaging_options = "exclude 'META-INF/services/javax.annotation.processing.Processor'", "exclude 'META-INF/*.version'"

# (bool) Copia bibliotecas em vez de criar libpymodules.so
android.copy_libs = 1

# (list) Arquiteturas suportadas
android.archs = arm64-v8a

# (bool) Permite backup automático (Android 6+)
android.allow_backup = True

# (str) Formato de saída no modo release
android.release_artifact = apk

# (bool) Modo debug ativo
android.debug = True

# (dict) Variáveis de ambiente para build do p4a
android.p4a_env = SHELL=/bin/bash,MAKEFLAGS=-j1

# (str) Bootstrap usado pelo p4a
p4a.bootstrap = sdl2

# (str) Python a usar no host
p4a.host_python = python3.9

# (str) URL do python-for-android
p4a.url = https://github.com/kivy/python-for-android.git

# (str) Branch do python-for-android
p4a.branch = develop

# (str) Diretório para receitas locais (opcional)
p4a.local_recipes = .buildozer/android/platform/python-for-android/recipes

# (bool) Usar setup.py (False evita erros desnecessários)
p4a.setup_py = false


[buildozer]

# (int) Nível de log (0=erro, 1=info, 2=debug)
log_level = 2

# (int) Mostrar aviso ao rodar como root
warn_on_root = 0

# (str) Diretório para artefatos do build
# build_dir = ./.buildozer

# (str) Diretório para saída do APK
# bin_dir = ./bin


[ios]

# (str) URL para kivy-ios
ios.kivy_ios_url = https://github.com/kivy/kivy-ios

# (str) Branch kivy-ios
ios.kivy_ios_branch = master

# (str) URL do ios-deploy
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy

# (str) Branch ios-deploy
ios.ios_deploy_branch = 1.10.0

# (bool) Permitir assinatura (False em builds automáticos)
ios.codesign.allowed = false

