"use client";
import { useState } from "react";
import { createNote } from "@/lib/api";
import { useRouter } from "next/navigation";

export default function CreateNotePage() {
    const [content, setContent] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await createNote(content);
        router.push("/");
    };

    return (
        <div className="min-h-screen flex items-center justify-center">
            <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-bold mb-4">Create a Note</h2>
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    className="w-full border rounded-lg p-2 mb-4"
                    placeholder="Write something..."
                    required
                />
                <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-md">
                    Save Note
                </button>
            </form>
        </div>
    );
}
