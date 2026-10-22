---
title: VS Code Setup
---

Use the **WPILib 2026 VS Code** installed by the WPILib installer. Install the VMX2026 `.vsix` as described in [Install WPILib and VMX2026](software-install.md).

1. Open a WPILib 2026 robot project or create a new C++ or Java project.
2. Open the Command Palette with **Ctrl+Shift+P**.
3. Run **VMX2026: Change the deploy target to VMX-Pi (from RoboRIO)**.
4. Run **VMX2026: Update VMX2026 Version** to connect the project to a compatible GradleRIO and VMX HAL release pair.
5. Build and deploy with the project's Gradle wrapper:

   ```sh
   ./gradlew build
   ./gradlew deploy -PteamNumber=1234
   ```

   Replace `1234` with your team number. The deploy target defaults to the `ubuntu` account; set `VMX_USER` or `VMX_PASSWORD` if the robot credentials differ.

The extension supports WPILib 2026 Groovy `build.gradle` projects with one deploy target. Kotlin DSL, WPILib 2020 projects, and projects with multiple targets are not supported.

## Prepare for offline builds

While the development computer has Internet access, run **VMX2026: Save VMX2026 Offline**. It downloads and resolves project dependencies, builds online, then verifies a forced offline build. After this succeeds, the project can build with Gradle's `--offline` option. Run the command again after changing dependencies, vendor libraries, or the deploy target.

If an offline build reports that a dependency is not cached, connect to the Internet and run **Save VMX2026 Offline** before deploying offline.
