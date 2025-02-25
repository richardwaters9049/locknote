"use client";
import { useEffect, useState } from "react";
import NoteList from "@/components/NoteList";
import { fetchNotes } from "@/lib/api";

export default function Home() {
  const [notes, setNotes] = useState<string[]>([]);

  useEffect(() => {
    fetchNotes().then(setNotes).catch(console.error);
  }, []);

  return (
    <div className="min-h-screen p-8 bg-gray-100">
      <h1 className="text-3xl font-bold text-center mb-4 text-black">Secure Notes</h1>
      <NoteList notes={notes} />
    </div>
  );
}
