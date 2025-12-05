# This is a separate python file because you might want to extract outside data.
# Write your own update logs below.
import Internals.Configuration as config

logs = f"""

**📅 (12/12/2024)**
    > 🟢 Added update logs command.
    > 🧊 New ability system, when defeating ice bosses, you will get the ice ability, more abilities will be added soon.
    > 🔨 Finished rebalancing boss power.
    > 📈 Added {config.getconfig("VoteCommand")} command to vote the application on Top.GG and get rewards.
**📅 (12/13/2024)**
    > 🔨 Fixed leaderboard not listing members properly.
**📅 (12/22/2024)**
    > 🛠️ Overhauled the {config.getconfig("VoteCommand")} command.
**📅 (12/28/2024)**
    > 🔴 Removed ability system.
    > ✨ Improved the battle panel design.
    > 🌲 Added ember {config.getconfig("FarmCommand")}s to compensate for the removal of abilities.
    > 🛠️ Adjusted the report command to allow ember farming.
**📅 (1/7/2025)**
    > 📃 Leaderboards will now show member usernames instead of display names.
**📅 (1/17/2025)**
    > ⚙️ Fixed the {config.getconfig("LeaderBoardCommand")} command.
**📅 (3/22/2025)**
    __👀 (Developer Note):__ I understand that an update took a long time to come, a rewrite of this application is planned, expect it 1 - 3 month(s) from now. I promise it will be much better, for now, I can keep adding more small features from the community.
    > 🧠 Added new {config.getconfig("SuggestCommand")} command.
**📅 (4/11/2025)**
    > ⚡ Optimized the application further, expect a performance boost. This is first part of the rewrite. Fun gameplay updates are planned.
"""