# 2020
Making dat app, doe

# Exporting 2020 project scripts
To use the shell scripts inside the _script folders, include the following to your `.bash_profile`:

```
export PATH="$HOME/*<your local directory to your project 2020 folder>*/_scripts:$PATH"
```
You can run the **2020** commands:
- Start the server with `2020 server`
- Start the client with `2020 client`
- Start the debug client on web with `2020 debug`

# Building and running on simulator

Be sure @capacitor/core @capacitor/cli is installed.
```
cd client
npm install @capacitor/core @capacitor/cli
```

To make sure you have these packages installed, run:
```
npm list @capacitor/core @capacitor/cli
```

If npm throws an error/cannot find these packages, run:
```
npm install --save @capacitor/core @capacitor/cli
```

Add ios platform with (only need to do this once to create the `ios` directory)
```
npx cap add ios
```

Launch XCode with:
```
npx cap open ios
```