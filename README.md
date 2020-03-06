# 2020
Making dat app, doe

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