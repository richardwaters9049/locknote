type NoteListProps = {
    notes: string[];
};

export default function NoteList({ notes }: NoteListProps) {
    return (
        <ul className="max-w-2xl mx-auto bg-white p-4 rounded-lg shadow-md">
            {notes.length > 0 ? (
                notes.map((note, index) => (
                    <li key={index} className="border-b py-2">
                        {note}
                    </li>
                ))
            ) : (
                <p className="text-gray-500 text-center">No notes yet.</p>
            )}
        </ul>
    );
}
