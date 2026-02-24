import re

with open('/Users/lucifer/Music/portfolio new/index31.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We will search for the timeline section
start_marker = '<section id="timeline"'
end_marker = '</section>'

start_idx = content.find(start_marker)
# Find the next </section> after start_idx
end_idx = content.find(end_marker, start_idx) + len(end_marker)

timeline_section = content[start_idx:end_idx]

# Replace the inner part: we'll rebuild the timeline items.
# We just need to replace the 5 items.
new_items = """
            <h2 class="text-3xl font-bold text-white mb-16 text-center">
                Professional <span class="text-cyan-400">Path</span>
            </h2>

            <div class="relative border-l border-slate-800 ml-4 md:ml-0 space-y-16">

                <!-- 1️⃣ CURRENT ROLE -->
                <div class="relative pl-8 md:pl-0 md:flex items-center group">
                    <div
                        class="absolute -left-[5px] md:left-1/2 md:-ml-[5px] w-3 h-3 rounded-full bg-cyan-500 shadow-[0_0_10px_rgba(6,182,212,0.6)] z-10">
                    </div>

                    <div class="hidden md:block w-1/2 pr-12 text-right">
                        <div class="glass-card p-6 rounded-xl border-r-4 border-r-cyan-500 hover:border-r-cyan-400 transition-colors">
                            <h3 class="text-lg font-bold text-white">Associate</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Nor’easters team supporting BL Quote & Contract DEVO with XML ingestion,
                                automation workflows and data integrity validations.
                            </p>
                        </div>
                    </div>

                    <div class="w-full md:w-1/2 md:pl-12 text-left">
                        <span class="hidden md:block font-mono text-cyan-400 text-sm">01/2026 - Present</span>
                        <div class="md:hidden glass-card p-6 rounded-xl border-l-4 border-l-cyan-500 transition-colors">
                            <span class="block font-mono text-cyan-400 text-xs mb-2">01/2026 - Present</span>
                            <h3 class="text-lg font-bold text-white">Associate</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Nor’easters team supporting BL Quote & Contract DEVO with XML ingestion,
                                automation workflows and data integrity validations.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 2️⃣ ASSOCIATE (ShiftX) -->
                <div class="relative pl-8 md:pl-0 md:flex items-center group">
                    <div
                        class="absolute -left-[5px] md:left-1/2 md:-ml-[5px] w-3 h-3 rounded-full bg-slate-600 group-hover:bg-cyan-500 transition-colors z-10">
                    </div>

                    <div class="hidden md:block w-1/2 pr-12 text-right">
                        <span class="font-mono text-slate-500 text-sm">07/2025 - 12/2025</span>
                    </div>

                    <div class="w-full md:w-1/2 md:pl-12">
                        <div class="glass-card p-6 rounded-xl border-l-4 border-l-slate-600 hover:border-l-cyan-500 transition-colors">
                            <span class="md:hidden block font-mono text-slate-500 text-xs mb-2">07/2025 - 12/2025</span>
                            <h3 class="text-lg font-bold text-white">Associate</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Developer in ShiftX-1B migration resiliency initiative.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 3️⃣ PROGRAMMER ANALYST -->
                <div class="relative pl-8 md:pl-0 md:flex items-center group">
                    <div class="absolute -left-[5px] md:left-1/2 md:-ml-[5px] w-3 h-3 rounded-full bg-slate-700 z-10">
                    </div>

                    <div class="hidden md:block w-1/2 pr-12 text-right">
                        <div class="glass-card p-6 rounded-xl border-r-4 border-r-slate-700 hover:border-r-cyan-400 transition-colors">
                            <h3 class="text-lg font-bold text-white">Programmer Analyst</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Core Developer in Project FTL (Snowflake Consolidation). Implemented CDC pipelines.
                            </p>
                        </div>
                    </div>

                    <div class="w-full md:w-1/2 md:pl-12 text-left">
                        <span class="hidden md:block font-mono text-slate-600 text-sm">04/2024 - 07/2025</span>
                        <div class="md:hidden glass-card p-6 rounded-xl border-l-4 border-l-slate-700 transition-colors">
                            <span class="block font-mono text-slate-600 text-xs mb-2">04/2024 - 07/2025</span>
                            <h3 class="text-lg font-bold text-white">Programmer Analyst</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Core Developer in Project FTL (Snowflake Consolidation). Implemented CDC pipelines.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 4️⃣ PROGRAMMER ANALYST TRAINEE -->
                <div class="relative pl-8 md:pl-0 md:flex items-center group">
                    <div class="absolute -left-[5px] md:left-1/2 md:-ml-[5px] w-3 h-3 rounded-full bg-slate-700 z-10">
                    </div>

                    <div class="hidden md:block w-1/2 pr-12 text-right">
                        <span class="font-mono text-slate-600 text-sm">08/2023 - 12/2024</span>
                    </div>

                    <div class="w-full md:w-1/2 md:pl-12">
                        <div class="glass-card p-6 rounded-xl border-l-4 border-l-slate-700 hover:border-l-cyan-400 transition-colors">
                            <span class="md:hidden block font-mono text-slate-600 text-xs mb-2">08/2023 - 12/2024</span>
                            <h3 class="text-lg font-bold text-white">Programmer Analyst Trainee</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                L1 Support for Project Liberty Andes.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- 5️⃣ INTERN -->
                <div class="relative pl-8 md:pl-0 md:flex items-center group">
                    <div
                        class="absolute -left-[5px] md:left-1/2 md:-ml-[5px] w-3 h-3 rounded-full bg-blue-500 shadow-[0_0_10px_rgba(59,130,246,0.5)] z-10">
                    </div>

                    <div class="hidden md:block w-1/2 pr-12 text-right">
                        <div
                            class="glass-card p-6 rounded-xl border-r-4 border-r-blue-500 hover:border-r-cyan-400 transition-colors">
                            <h3 class="text-lg font-bold text-white">Intern (Microsoft Azure)</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Completed training & acquired practical experience in cloud computing.
                            </p>
                        </div>
                    </div>

                    <div class="w-full md:w-1/2 md:pl-12 text-left">
                        <span class="hidden md:block font-mono text-blue-400 text-sm">03/2022 - 07/2022</span>
                        <div class="md:hidden glass-card p-6 rounded-xl border-l-4 border-l-blue-500 transition-colors">
                            <span class="block font-mono text-blue-400 text-xs mb-2">03/2022 - 07/2022</span>
                            <h3 class="text-lg font-bold text-white">Intern (Microsoft Azure)</h3>
                            <p class="text-sm text-slate-400 mt-2">
                                Completed training & acquired practical experience in cloud computing.
                            </p>
                        </div>
                    </div>
                </div>

            </div>
"""

new_timeline_section = '<section id="timeline" class="py-24 max-w-4xl mx-auto section-spy">\n' + new_items + '\n        </section>'

new_content = content[:start_idx] + new_timeline_section + content[end_idx:]

with open('/Users/lucifer/Music/portfolio new/index31.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated timeline successfully.")
