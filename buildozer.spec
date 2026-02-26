[app]

# (str) Title of your application
title = VocabularyAutomation

# (str) Package name
package.name = vocabularyautomation

# (str) Package domain (needed for android/ios packaging)
package.domain = com.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,pillow

# (list) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY


#
# OSX Specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, use a git checkout of kivy-ios
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master

# (bool) Whether or not to sign the code
#ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s


#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names: black, blue, green, lime, red, white, yellow
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/ for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,SYSTEM_ALERT_WINDOW,BIND_ACCESSIBILITY_SERVICE,WAKE_LOCK,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CAMERA,FOREGROUND_SERVICE

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# 自动接受Android SDK许可证（与现有镜像源配置合并）

# 设置环境变量自动接受许可证
android.env = ANDROID_ACCEPT_SDK_LICENSES=yes ANDROID_SDK_HOME=/home/runner/.android

# (str) Android NDK version to use
android.ndk = 25

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = True

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to add permissions or other manifest elements
#android.extra_manifest_xml = <uses-permission android:name="android.permission.CAMERA" />

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to add custom entries like activities, providers, etc.
#android.extra_manifest_application_children = <activity android:name=".AnotherActivity" />

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class instead of PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = @android:style/Theme.Holo.Light

# (list) Pattern to whitelist for the whole project
#android.whitelist = 

# (str) Path to a custom whitelist file
#android.whitelist_src = 

# (str) Path to a custom blacklist file
#android.blacklist_src = 

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process.
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src = 

# (list) Android AAR archives to add (currently works only with sdl2_gradle
# bootstrap)
#android.add_aars = 

# (list) Gradle dependencies to add (currently works only with sdl2_gradle
# bootstrap)
#android.gradle_dependencies = 

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes
# android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"

# (list) packaging options to add
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters = 

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# 添加无障碍服务配置
android.extra_manifest_xml = <service android:name="org.kivy.android.PythonService" android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE" android:exported="true">
    <intent-filter>
        <action android:name="android.accessibilityservice.AccessibilityService" />
    </intent-filter>
    <meta-data android:name="android.accessibilityservice" android:resource="@xml/accessibility_service_config" />
</service>

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data = 

# (list) Android library project to add (will be added in the 
# project.properties automatically.)
#android.library_references = 

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library = 

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = armeabi-v7a, arm64-v8a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules = 

# (str) If you need to insert variables into your AndroidManifest.xml file, 
# you can do so with the manifestPlaceholders property. 
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:"org.kivy.customurl"]
android.manifest_placeholders = [appAuthRedirectScheme:com.example.vocabulary]


#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes = %(source.dir)s/recipes

# (str) Filename to the hook for p4a
#p4a.hook = %(source.dir)s/p4a_hook.py

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port = 

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future, this will default to --use-setup-py in order to be consistent with pip"
p4a.setup_py = true

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
p4a.extra_args = --index-url=https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host=pypi.tuna.tsinghua.edu.cn --accept-android-sdk-licenses --accept-android-ndk-licenses



#
# iOS specific
#

# (str) Path to a custom kivy-ios
#ios.kivy_ios_dir = ../kivy-ios

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) Commands to execute when the iOS simulator is started
#ios.simulator.startup_commands = xcrun simctl openurl booted com.apple.mobilesafari https://kivy.org

# (str) Path to the root of the ios directory
#ios.native_directory = %(source.dir)s/ios

# (bool) Whether or not to use CocoaPods
#ios.cocoapods = True

# (bool) Whether or not to use the Swift compiler when building the private frameworks
#ios.swift_version = 5


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
# bin_dir = ./bin

# (list) The list of keyring names to use when decrypting secrets
# see https://buildozer.readthedocs.io/en/latest/encrypted-secrets.html
# buildozer.secrets.keyring = ['buildozer']

# (str) If specified, this key will be used to decrypt secrets and keep them in memory
# buildozer.secrets.password = 

# (list) A list of module to import at start time
# modules = ordereddict

# (str) Set the loghandler and formatter to use
# loghandler = [('buildozer', 'DEBUG', '%(message)s')]

# (bool) Display all log messages of all loggers
# logall = True

# (bool) If False, buildozer will delete the build directory on failure
# keep_build = False

# (str) Path to buildozer configuration file
# config = ~/.buildozer/default.spec

# (bool) Set to True if you want to use the buildcache
# If this is True, buildozer will use a cache of generated
# build artifacts to speed up the build process
# buildcache = False

# (str) Path to the buildcache directory
# buildcache_dir = ./.buildozer/cache

# (str) Command line arguments to be passed to p4a
# p4a_args = 

# (str) Command line arguments to be passed to apktool
# apktool_args = 

# (str) Command line arguments to be passed to aapt
# aapt_args = 

# (str) Command line arguments to be passed to aidl
# aidl_args = 

# (str) Command line arguments to be passed to zipalign
# zipalign_args = 

# (str) Command line arguments to be passed to jarsigner
# jarsigner_args = 

# (str) Command line arguments to be passed to the Android Asset Packaging Tool (aapt2)
# aapt2_args = 

# (str) Command line arguments to be passed to the Android Resource Compiler (aapt2)
# arsc_args = 

# (str) Command line arguments to be passed to the Android Debug Bridge (adb)
# adb_args = 

# (str) Command line arguments to be passed to the Android Emulator (emulator)
# emulator_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (ndk-build)
# ndk_build_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (ndk-gcc)
# ndk_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (ndk-g++)
# ndk_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (clang)
# clang_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (clang++)
# clangpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (lld)
# lld_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (llvm-objdump)
# llvm_objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (llvm-readelf)
# llvm_readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (llvm-strip)
# llvm_strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (llvm-symbolizer)
# llvm_symbolizer_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (objcopy)
# objcopy_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (objdump)
# objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (readelf)
# readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (strip)
# strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (strings)
# strings_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-addr2line)
# addr2line_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-ar)
# ar_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-as)
# as_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-c++filt)
# cxxfilt_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-elfedit)
# elfedit_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc)
# gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++)
# gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcov)
# gcov_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gprof)
# gprof_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-ld)
# ld_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-nm)
# nm_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-objcopy)
# objcopy_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-objdump)
# objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-ranlib)
# ranlib_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-readelf)
# readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-size)
# size_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-strings)
# strings_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-strip)
# strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-addr2line)
# addr2line_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-addr2line)
# aarch64_addr2line_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-ar)
# aarch64_ar_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-as)
# aarch64_as_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-c++filt)
# aarch64_cxxfilt_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-elfedit)
# aarch64_elfedit_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-gcc)
# aarch64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-g++)
# aarch64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-gcov)
# aarch64_gcov_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-gprof)
# aarch64_gprof_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-ld)
# aarch64_ld_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-nm)
# aarch64_nm_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-objcopy)
# aarch64_objcopy_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-objdump)
# aarch64_objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-ranlib)
# aarch64_ranlib_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-readelf)
# aarch64_readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-size)
# aarch64_size_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-strings)
# aarch64_strings_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-strip)
# aarch64_strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-addr2line)
# x86_64_addr2line_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-ar)
# x86_64_ar_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-as)
# x86_64_as_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-c++filt)
# x86_64_cxxfilt_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-elfedit)
# x86_64_elfedit_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc)
# x86_64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++)
# x86_64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcov)
# x86_64_gcov_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gprof)
# x86_64_gprof_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-ld)
# x86_64_ld_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-nm)
# x86_64_nm_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-objcopy)
# x86_64_objcopy_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-objdump)
# x86_64_objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-ranlib)
# x86_64_ranlib_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-readelf)
# x86_64_readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-size)
# x86_64_size_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-strings)
# x86_64_strings_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-strip)
# x86_64_strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-addr2line)
# i686_addr2line_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-ar)
# i686_ar_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-as)
# i686_as_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-c++filt)
# i686_cxxfilt_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-elfedit)
# i686_elfedit_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc)
# i686_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++)
# i686_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcov)
# i686_gcov_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gprof)
# i686_gprof_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-ld)
# i686_ld_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-nm)
# i686_nm_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-objcopy)
# i686_objcopy_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-objdump)
# i686_objdump_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-ranlib)
# i686_ranlib_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-readelf)
# i686_readelf_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-size)
# i686_size_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-strings)
# i686_strings_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-strip)
# i686_strip_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-w64-mingw32-gcc)
# mingw64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-w64-mingw32-g++)
# mingw64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-w64-mingw32-gcc)
# mingw32_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-w64-mingw32-g++)
# mingw32_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-gnueabihf-gcc)
# armhf_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-gnueabihf-g++)
# armhf_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-gnu-gcc)
# aarch64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-gnu-g++)
# aarch64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-gnu-gcc)
# x86_64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-gnu-g++)
# x86_64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-gnu-gcc)
# i686_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-gnu-g++)
# i686_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (mips-linux-gnu-gcc)
# mips_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (mips-linux-gnu-g++)
# mips_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (mips64-linux-gnuabi64-gcc)
# mips64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (mips64-linux-gnuabi64-g++)
# mips64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (powerpc64le-linux-gnu-gcc)
# ppc64le_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (powerpc64le-linux-gnu-g++)
# ppc64le_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (s390x-linux-gnu-gcc)
# s390x_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (s390x-linux-gnu-g++)
# s390x_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (riscv64-linux-gnu-gcc)
# riscv64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (riscv64-linux-gnu-g++)
# riscv64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (sparc64-linux-gnu-gcc)
# sparc64_gcc_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (sparc64-linux-gnu-g++)
# sparc64_gpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-ld.bfd)
# arm_ld_bfd_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-ld.bfd)
# aarch64_ld_bfd_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-ld.bfd)
# x86_64_ld_bfd_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-ld.bfd)
# i686_ld_bfd_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-ld.gold)
# arm_ld_gold_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-ld.gold)
# aarch64_ld_gold_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-ld.gold)
# x86_64_ld_gold_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-ld.gold)
# i686_ld_gold_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-clang)
# arm_clang_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-clang)
# aarch64_clang_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-clang)
# x86_64_clang_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-clang)
# i686_clang_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-clang++)
# arm_clangpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-clang++)
# aarch64_clangpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-clang++)
# x86_64_clangpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-clang++)
# i686_clangpp_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.9)
# arm_gcc49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.9)
# arm_gpp49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-gcc-4.9)
# aarch64_gcc49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-g++-4.9)
# aarch64_gpp49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.9)
# x86_64_gcc49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.9)
# x86_64_gpp49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.9)
# i686_gcc49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.9)
# i686_gpp49_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.8)
# arm_gcc48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.8)
# arm_gpp48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-gcc-4.8)
# aarch64_gcc48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (aarch64-linux-android-g++-4.8)
# aarch64_gpp48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.8)
# x86_64_gcc48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.8)
# x86_64_gpp48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.8)
# i686_gcc48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.8)
# i686_gpp48_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.7)
# arm_gcc47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.7)
# arm_gpp47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.7)
# x86_64_gcc47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.7)
# x86_64_gpp47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.7)
# i686_gcc47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.7)
# i686_gpp47_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.6)
# arm_gcc46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.6)
# arm_gpp46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.6)
# x86_64_gcc46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.6)
# x86_64_gpp46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.6)
# i686_gcc46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.6)
# i686_gpp46_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.4.3)
# arm_gcc44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.4.3)
# arm_gpp44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.4.3)
# x86_64_gcc44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.4.3)
# x86_64_gpp44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.4.3)
# i686_gcc44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.4.3)
# i686_gpp44_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.3.3)
# arm_gcc43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.3.3)
# arm_gpp43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.3.3)
# x86_64_gcc43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.3.3)
# x86_64_gpp43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.3.3)
# i686_gcc43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.3.3)
# i686_gpp43_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.2.1)
# arm_gcc42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.2.1)
# arm_gpp42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.2.1)
# x86_64_gcc42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.2.1)
# x86_64_gpp42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.2.1)
# i686_gcc42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.2.1)
# i686_gpp42_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.1.2)
# arm_gcc41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.1.2)
# arm_gpp41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.1.2)
# x86_64_gcc41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.1.2)
# x86_64_gpp41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.1.2)
# i686_gcc41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.1.2)
# i686_gpp41_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-4.0.3)
# arm_gcc40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-4.0.3)
# arm_gpp40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-4.0.3)
# x86_64_gcc40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-4.0.3)
# x86_64_gpp40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-4.0.3)
# i686_gcc40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-4.0.3)
# i686_gpp40_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-3.4.5)
# arm_gcc34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-3.4.5)
# arm_gpp34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-3.4.5)
# x86_64_gcc34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-3.4.5)
# x86_64_gpp34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-3.4.5)
# i686_gcc34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-3.4.5)
# i686_gpp34_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-3.3.2)
# arm_gcc33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-3.3.2)
# arm_gpp33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-3.3.2)
# x86_64_gcc33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-3.3.2)
# x86_64_gpp33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-3.3.2)
# i686_gcc33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-3.3.2)
# i686_gpp33_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-3.2.3)
# arm_gcc32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-3.2.3)
# arm_gpp32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-3.2.3)
# x86_64_gcc32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-3.2.3)
# x86_64_gpp32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-3.2.3)
# i686_gcc32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-3.2.3)
# i686_gpp32_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-3.1)
# arm_gcc31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-3.1)
# arm_gpp31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-3.1)
# x86_64_gcc31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-3.1)
# x86_64_gpp31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-3.1)
# i686_gcc31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-3.1)
# i686_gpp31_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-gcc-3.0)
# arm_gcc30_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (arm-linux-androideabi-g++-3.0)
# arm_gpp30_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-gcc-3.0)
# x86_64_gcc30_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (x86_64-linux-android-g++-3.0)
# x86_64_gpp30_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-gcc-3.0)
# i686_gcc30_args = 

# (str) Command line arguments to be passed to the Android NDK Toolchain (i686-linux-android-g++-3.0)
# i686_gpp30_args = 
